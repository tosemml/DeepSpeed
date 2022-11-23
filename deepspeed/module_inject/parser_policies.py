import re


# yapf: disable
class ParserPolicies():
    parser_policy_map = dict(
        albert=dict(AlbertLayer=(".ffn_output", "attention.dense", ), ),
        bart=dict(BartEncoderLayer=(".fc2", "self_attn.out_proj", ), BartDecoderLayer=(".fc2", "encoder_attn.out_proj", "self_attn.out_proj", ), ),
        beit=dict(BeitLayer=("intermediate.dense", "output.dense", "attention.value", ), ),
        bert=dict(BertLayer=("self.value", "output.dense", ), ),
        bert_generation=dict(BertGenerationLayer=("output.dense", "self.value", ), ),
        big_bird=dict(BigBirdLayer=("self.value", "output.dense", ), ),
        bigbird_pegasus=dict(BigBirdPegasusEncoderLayer=("self_attn.output", ".fc2", "self.value", ), BigBirdPegasusDecoderLayer=("self_attn.out_proj", ".fc2", "encoder_attn.out_proj", ), ),
        blenderbot=dict(BlenderbotEncoderLayer=(".fc2", "self_attn.out_proj", ), BlenderbotDecoderLayer=(".fc2", "self_attn.out_proj", "encoder_attn.out_proj", ), ),
        blenderbot_small=dict(BlenderbotSmallEncoderLayer=("self_attn.out_proj", ".fc2", ), BlenderbotSmallDecoderLayer=("self_attn.out_proj", ".fc2", "encoder_attn.out_proj", ), ),
        bloom=dict(BloomBlock=("self_attention.dense", "mlp.dense_4h_to_h", ), ),
        camembert=dict(CamembertLayer=("self.value", "output.dense", ), ),
        canine=dict(CanineLayer=("output.dense", "self.value", ), ),
        clip=dict(CLIPEncoderLayer=("mlp.fc2", "self_attn.out_proj", ), ),
        codegen=dict(CodeGenBlock=("mlp.fc_out", "attn.out_proj", ), ),
        conditional_detr=dict(ConditionalDetrDecoderLayer=("encoder_attn.out_proj", ".fc2", "self_attn.out_proj", ), ConditionalDetrEncoderLayer=(".fc2", "self_attn.out_proj", ), ),
        convbert=dict(ConvBertLayer=("output.dense", "self.conv_out_layer", ), ),
        ctrl=dict(EncoderLayer=("multi_head_attention.dense", ), ),
        data2vec_audio=dict(Data2VecAudioEncoderLayer=("feed_forward.output_dense", "attention.out_proj", ), ),
        data2vec_text=dict(Data2VecTextLayer=("self.value", "output.dense", ), ),
        data2vec_vision=dict(Data2VecVisionLayer=("intermediate.dense", "attention.value", "output.dense", ), ),
        deberta=dict(DebertaLayer=("self.pos_q_proj", "output.dense", ), ),
        deberta_v2=dict(DebertaV2Layer=("self.pos_query_proj", "output.dense", ), ),
        deformable_detr=dict(DeformableDetrEncoderLayer=("self_attn.output_proj", ".fc2", ), DeformableDetrDecoderLayer=("encoder_attn.output_proj", ".fc2", "self_attn.out_proj", ), ),
        deit=dict(DeiTLayer=("output.dense", "intermediate.dense", "attention.value", ), ),
        detr=dict(DetrEncoderLayer=("self_attn.out_proj", ".fc2", ), DetrDecoderLayer=("encoder_attn.out_proj", "self_attn.out_proj", ".fc2", ), ),
        distilbert=dict(TransformerBlock=("attention.out_lin", "ffn.lin2", ), ),
        donut_swin=dict(DonutSwinLayer=("output.dense", "intermediate.dense", "self.value", ), ),
        dpt=dict(DPTViTLayer=("output.dense", "attention.value", "intermediate.dense", ), ),
        electra=dict(ElectraLayer=("self.value", "output.dense", ), ),
        ernie=dict(ErnieLayer=("output.dense", "self.value", ), ),
        esm=dict(EsmLayer=("intermediate.dense", "self.value", "output.dense", ), ),
        flava=dict(FlavaLayer=("attention.value", "intermediate.dense", "output.dense", ), ),
        fnet=dict(FNetLayer=("output.dense", ), ),
        fsmt=dict(DecoderLayer=(".fc2", "self_attn.out_proj", "encoder_attn.out_proj", ), EncoderLayer=(".fc2", "self_attn.out_proj", ), ),
        funnel=dict(FunnelLayer=("ffn.linear_2", "attention.post_proj", ), ),
        gpt_neo=dict(GPTNeoBlock=("mlp.c_proj", "attention.out_proj", ), ),
        gpt_neox=dict(GPTNeoXLayer=("attention.dense", "mlp.dense_4h_to_h", ), ),
        gpt_neox_japanese=dict(GPTNeoXJapaneseLayer=("mlp.dense_4h_to_h", "attention.dense", ), ),
        gptj=dict(GPTJBlock=("attn.out_proj", "mlp.fc_out", ), ),
        groupvit=dict(GroupViTEncoderLayer=("mlp.fc2", "self_attn.out_proj", ), GroupViTStage=("assign.proj", "mlp.fc2", "mlp_channels.fc2", "attn.out_proj", ), ),
        hubert=dict(HubertEncoderLayer=("attention.out_proj", "feed_forward.output_dense", ), HubertEncoderLayerStableLayerNorm=("attention.out_proj", "feed_forward.output_dense", ), ),
        layoutlm=dict(LayoutLMLayer=("self.value", "output.dense", ), ),
        layoutlmv2=dict(LayoutLMv2Layer=("output.dense", "self.value", ), ),
        layoutlmv3=dict(LayoutLMv3Layer=("output.dense", "self.value", ), ),
        led=dict(LEDEncoderLayer=(".fc2", "self_attn.output", "longformer_self_attn.value_global", ), LEDDecoderLayer=(".fc2", "self_attn.out_proj", "encoder_attn.out_proj", ), ),
        lilt=dict(LiltLayer=("output.dense", "layout_output.dense", "self.layout_value", ), ),
        longformer=dict(LongformerLayer=("output.dense", "self.value_global", ), ),
        longt5=dict(LongT5Block=("EncDecAttention.o", "DenseReluDense.wo", ), ),
        luke=dict(LukeLayer=("self.e2e_query", "output.dense", ), ),
        lxmert=dict(LxmertLayer=("output.dense", "self.value", ), ),
        m2m_100=dict(M2M100DecoderLayer=("self_attn.out_proj", "encoder_attn.out_proj", ".fc2", ), M2M100EncoderLayer=("self_attn.out_proj", ".fc2", ), ),
        marian=dict(MarianDecoderLayer=("encoder_attn.out_proj", ".fc2", "self_attn.out_proj", ), MarianEncoderLayer=(".fc2", "self_attn.out_proj", ), ),
        markuplm=dict(MarkupLMLayer=("self.value", "output.dense", ), ),
        maskformer=dict(MaskFormerSwinBlock=("output.dense", "self.value", "intermediate.dense", ), DetrDecoderLayer=(".fc2", "self_attn.out_proj", "encoder_attn.out_proj", ), ),
        mbart=dict(MBartDecoderLayer=(".fc2", "encoder_attn.out_proj", "self_attn.out_proj", ), MBartEncoderLayer=(".fc2", "self_attn.out_proj", ), ),
        mctct=dict(MCTCTLayer=("output.dense", "self.value", ), ),
        megatron_bert=dict(MegatronBertLayer=("self.value", "output.dense", "intermediate.dense", ), ),
        mobilebert=dict(FFNLayer=("output.dense", ), MobileBertLayer=("attention.dense", "output.dense", "input.dense", "bottleneck.dense", ), ),
        mpnet=dict(MPNetLayer=("attn.o", "output.dense", ), ),
        mvp=dict(MvpEncoderLayer=(".fc2", "self_attn.out_proj", ), MvpDecoderLayer=("encoder_attn.out_proj", ".fc2", "self_attn.out_proj", ), ),
        nezha=dict(NezhaLayer=("output.dense", "self.value", ), ),
        nystromformer=dict(NystromformerLayer=("output.dense", "self.value", ), ),
        opt=dict(OPTDecoderLayer=("self_attn.out_proj", ".fc2", ), ),
        owlvit=dict(OwlViTEncoderLayer=("self_attn.out_proj", "mlp.fc2", ), ),
        pegasus=dict(PegasusDecoderLayer=(".fc2", "self_attn.out_proj", "encoder_attn.out_proj", ), PegasusEncoderLayer=(".fc2", "self_attn.out_proj", ), ),
        pegasus_x=dict(PegasusXDecoderLayer=("encoder_attn.out_proj", "self_attn.out_proj", ".fc2", ), ),
        plbart=dict(PLBartDecoderLayer=(".fc2", "self_attn.out_proj", "encoder_attn.out_proj", ), PLBartEncoderLayer=(".fc2", "self_attn.out_proj", ), ),
        prophetnet=dict(ProphetNetEncoderLayer=("feed_forward.output", "self_attn.out_proj", ), ProphetNetDecoderLayer=("feed_forward.output", "self_attn.relative_pos_embeddings", "cross_attn.out_proj", ), ),
        realm=dict(RealmLayer=("self.value", "output.dense", ), ),
        reformer=dict(ReformerLayer=("output.dense", "dense.dense", "self_attention.value", ), ),
        rembert=dict(RemBertLayer=("output.dense", "self.value", ), ),
        roberta=dict(RobertaLayer=("self.value", "output.dense", ), ),
        roformer=dict(RoFormerLayer=("self.value", "output.dense", ), ),
        sew=dict(SEWEncoderLayer=("attention.out_proj", "feed_forward.output_dense", ), ),
        sew_d=dict(SEWDLayer=("self.pos_query_proj", "output.dense", ), ),
        speech_to_text=dict(Speech2TextDecoderLayer=("encoder_attn.out_proj", "self_attn.out_proj", ".fc2", ), Speech2TextEncoderLayer=("self_attn.out_proj", ".fc2", ), ),
        speech_to_text_2=dict(Speech2Text2DecoderLayer=("encoder_attn.out_proj", ".fc2", "self_attn.out_proj", ), ),
        splinter=dict(SplinterLayer=("self.value", "output.dense", ), ),
        swin=dict(SwinLayer=("output.dense", "intermediate.dense", "self.value", ), ),
        swinv2=dict(Swinv2Layer=("intermediate.dense", "self.value", "output.dense", ), ),
        t5=dict(T5Block=("DenseReluDense.wo", "SelfAttention.o", "EncDecAttention.o", ), ),
        table_transformer=dict(TableTransformerEncoderLayer=(".fc2", "self_attn.out_proj", ), TableTransformerDecoderLayer=(".fc2", "self_attn.out_proj", "encoder_attn.out_proj", ), ),
        tapas=dict(TapasLayer=("self.value", "output.dense", ), ),
        time_series_transformer=dict(TimeSeriesTransformerEncoderLayer=(".fc2", "self_attn.out_proj", ), TimeSeriesTransformerDecoderLayer=(".fc2", "encoder_attn.out_proj", "self_attn.out_proj", ), ),
        trajectory_transformer=dict(Block=(".l2", "attn.proj", ), ),
        trocr=dict(TrOCRDecoderLayer=(".fc2", "encoder_attn.out_proj", "self_attn.out_proj", ), ),
        unispeech=dict(UniSpeechEncoderLayer=("attention.out_proj", "feed_forward.output_dense", ), UniSpeechEncoderLayerStableLayerNorm=("attention.out_proj", "feed_forward.output_dense", ), ),
        unispeech_sat=dict(UniSpeechSatEncoderLayerStableLayerNorm=("attention.out_proj", "feed_forward.output_dense", ), UniSpeechSatEncoderLayer=("attention.out_proj", "feed_forward.output_dense", ), ),
        videomae=dict(VideoMAELayer=("intermediate.dense", "attention.value", "output.dense", ), ),
        vilt=dict(ViltLayer=("attention.value", "intermediate.dense", "output.dense", ), ),
        visual_bert=dict(VisualBertLayer=("output.dense", "self.value", ), ),
        vit=dict(ViTLayer=("intermediate.dense", "attention.value", "output.dense", ), ),
        vit_mae=dict(ViTMAELayer=("attention.value", "intermediate.dense", "output.dense", ), ),
        vit_msn=dict(ViTMSNLayer=("intermediate.dense", "attention.value", "output.dense", ), ),
        wav2vec2=dict(Wav2Vec2EncoderLayer=("attention.out_proj", "feed_forward.output_dense", ), Wav2Vec2EncoderLayerStableLayerNorm=("attention.out_proj", "feed_forward.output_dense", ), ),
        wav2vec2_conformer=dict(Wav2Vec2ConformerEncoderLayer=("ffn2.output_dense", "self_attn.linear_pos", "ffn1.output_dense", ), ),
        wavlm=dict(WavLMEncoderLayer=("feed_forward.output_dense", "attention.gru_rel_pos_linear", ), WavLMEncoderLayerStableLayerNorm=("feed_forward.output_dense", "attention.gru_rel_pos_linear", ), ),
        whisper=dict(WhisperDecoderLayer=("encoder_attn.out_proj", "self_attn.out_proj", ".fc2", ), WhisperEncoderLayer=("self_attn.out_proj", ".fc2", ), ),
        x_clip=dict(PromptGeneratorLayer=("cross_attn.proj", ), XCLIPVisionEncoderLayer=("message_attn.out_proj", "self_attn.out_proj", "mlp.fc2", ".message_fc", ), XCLIPEncoderLayer=("self_attn.out_proj", "mlp.fc2", ), ),
        xglm=dict(XGLMDecoderLayer=("self_attn.out_proj", "encoder_attn.out_proj", ".fc2", ), ),
        xlm_prophetnet=dict(XLMProphetNetDecoderLayer=("cross_attn.out_proj", "feed_forward.output", "self_attn.relative_pos_embeddings", ), XLMProphetNetEncoderLayer=("self_attn.out_proj", "feed_forward.output", ), ),
        xlm_roberta=dict(XLMRobertaLayer=("self.value", "output.dense", ), ),
        xlm_roberta_xl=dict(XLMRobertaXLLayer=("self.value", "intermediate.dense", "output.dense", ), ),
        xlnet=dict(XLNetLayer=("ff.layer_2", ), ),
        yolos=dict(YolosLayer=("intermediate.dense", "output.dense", "attention.value", ), ),
        yoso=dict(YosoLayer=("self.value", "output.dense", ), ),
    )

    def get_map_key(model):
        key = re.search(r": (.*?)Model", model)
        if key is None:
            key = re.search(r": (.*?)Stack", model)
        return key.group(1).lower()