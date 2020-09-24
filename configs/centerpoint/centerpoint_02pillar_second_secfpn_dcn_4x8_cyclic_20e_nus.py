_base_ = ['./centerpoint_02pillar_second_secfpn_4x8_cyclic_20e_nus.py']

model = dict(
    pts_bbox_head=dict(
        seperate_head=dict(
            type='DCNSeperateHead',
            dcn_config=dict(
                type='DCN',
                in_channels=64,
                out_channels=64,
                kernel_size=3,
                padding=1,
                groups=4,
                bias=True),
            init_bias=-2.19,
            final_kernel=3)))