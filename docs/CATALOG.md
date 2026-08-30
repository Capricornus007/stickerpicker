# 貼圖庫總目錄(Sticker Packs Catalog)

- 編纂日期:2026-08-30
- 資料來源:`/home/avatar/Downloads/stickerpicker/web/packs/` 下全部 54 個貼圖包 JSON(排除 `index.json`)
- 章節順序:依 `index.json` 的 `packs` 陣列排序,即貼圖選擇器的實際顯示順序
- 選擇器 homeserver:`https://matrix-client.matrix.org`(取自 `index.json` 的 `homeserver_url`)
- 縮圖目錄 `thumbnails/` 不在本目錄範圍內

## 一、全庫總計

| 統計項 | 數值 |
|---|---|
| 貼圖包數 | 54(其中 3 個空包:`USABest.json`、`kawaiikipfel_by_moe_sticker_bot.json`、`MygoStickerByAsahiRise.json`) |
| 貼圖總張數 | 3,149 |
| image/png | 2,996 張(95.1%) |
| video/webm | 150 張(4.8%) |
| image/gif | 3 張(0.1%) |
| 貼圖資料總位元組(各張 `info.size` 加總) | 627,892,500 B(約 598.8 MB) |
| 54 個包 JSON 檔案本身合計大小 | 1,525,611 B(約 1.5 MB) |
| 來源 ID 分佈 | Telegram(`tg-`)2,321 張;外部匯入(`sha256`)828 張 |
| 異常張(零尺寸或 <500 B) | 0 張 |

## 二、欄位與標記說明

每張貼圖一列,欄位為:`序號 | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID`。

- **大小(KB)**:取該張 `info.size` 除以 1024,四捨五入至小數一位。
- **尺寸(WxH)**:取該張 `info.w` x `info.h`;實際尺寸多樣(全庫共 370 種),非全部 256x256。
- **來源 ID**:
  - `tg-<數字>` — 自 Telegram 匯入的貼圖檔案 ID(完整列出)。
  - `sha256:<前 16 碼>…〔外〕` — 非 Telegram 來源(外部匯入/本機製作)的條目,以 `〔外〕` 標記,僅顯示雜湊前綴。
- **〔異〕**:零尺寸(`w`/`h` 為 0 或缺漏)或大小 <500 B 的異常貼圖,會在 body 欄前標記。本次盤點結果:**0 張**,全庫無此類條目。
- **已知校驗點**:`stneng.json` 先前已摘除一張 256x0 的畸形貼圖(`tg-692497273854099475`)。本次編纂已重新確認該張**不在**資料中;若目錄中出現它,代表讀到的是舊資料。

## 三、各包索引總表

<!-- PACK_INDEX_BEGIN -->
| 序 | 檔名 | 標題 | 張數 | 貼圖合計大小 |
|---:|---|---|---:|---:|
| 1 | `in_BCDGDC_by_NaiDrawBot.json` | in_BCDGDC_by_NaiDrawBot | 32 | 6,265,543 B |
| 2 | `ukuku1_2.json` | ukuku1_2 | 45 | 7,930,657 B |
| 3 | `ArcaeaLinkPlay.json` | ArcaeaLinkPlay | 46 | 14,049,408 B |
| 4 | `Archwizard_pack.json` | Archwizard_pack | 69 | 14,562,911 B |
| 5 | `CacheCI.json` | CacheCI | 107 | 20,473,338 B |
| 6 | `fuckgfwnewbie.json` | fuckgfwnewbie | 47 | 6,601,582 B |
| 7 | `suzumi_bili_2.json` | suzumi_bili_2 | 111 | 23,240,093 B |
| 8 | `NekoTempest.json` | NekoTempest | 73 | 15,378,859 B |
| 9 | `Qing_by_NaiDrawBot.json` | Qing_by_NaiDrawBot | 23 | 4,649,518 B |
| 10 | `Togawa_Sakiko_1b.json` | Togawa_Sakiko_1b | 20 | 4,853,865 B |
| 11 | `X264WebmPack.json` | X264WebmPack | 34 | 10,644,538 B |
| 12 | `b675aff8_by_fStikBot.json` | b675aff8_by_fStikBot | 101 | 18,694,330 B |
| 13 | `kirinfav_by_favorite_stickers_bot.json` | kirinfav_by_favorite_stickers_bot | 120 | 23,432,667 B |
| 14 | `yjsnpis.json` | YJSNPI_STICKERS | 55 | 10,664,130 B |
| 15 | `lmao9685.json` | lmao | 66 | 7,474,903 B |
| 16 | `wuyuan5.json` | 不关猫猫的事哦 @moonrenddev | 23 | 4,615,686 B |
| 17 | `GayPackbyAli_yhyee.json` | Gay?  @Ali_Yhyee_st | 30 | 3,309,901 B |
| 18 | `zakk_is_hentai_by_fStikBot.json` | Zakk 変態語錄 :: @fStikBot | 24 | 2,760,088 B |
| 19 | `in_AHDBEC_by_NaiDrawBot.json` | 阿库露 @zhaxia_cn | 64 | 16,137,442 B |
| 20 | `stickersandhuaji.json` | 全能表情包#(滑稽) | 39 | 6,056,130 B |
| 21 | `stneng.json` | s | 28 | 5,540,475 B |
| 22 | `ChinaTelecom.json` | 永远怀念 | 71 | 4,358,569 B |
| 23 | `cursedstickerspack_by_favorite_stickers_bot.json` | Cursed | 78 | 14,807,418 B |
| 24 | `hfssnpack_by_favorite_stickers_bot.json` | hfssnpack | 36 | 7,886,011 B |
| 25 | `CosmicPrincessKaguya1_by_NichistickerBot.json` | 超时空辉夜姬！(XHS:95047506868) | 36 | 4,686,064 B |
| 26 | `in_JHCGEC_by_NaiDrawBot.json` | 方糖小鼠鼠 @zhaxia_cn | 32 | 7,801,927 B |
| 27 | `lptoys.json` | lptoy | 68 | 14,695,333 B |
| 28 | `Qing_Stickers_Collection_1.json` | 晴の收藏① | 102 | 15,458,792 B |
| 29 | `SkipM44_2_by_fStikBot.json` | SkipM44贴纸2 | 98 | 20,044,041 B |
| 30 | `a01fe077_by_fStikBot.json` | TEmPTaTi♂N :: @fStikBot | 76 | 15,821,468 B |
| 31 | `in_DDBIDC_by_NaiDrawBot.json` | 小火切 @zhaxia_cn | 90 | 24,876,260 B |
| 32 | `fa1_qing2_san4_hua2_by_fStikBot.json` | 嘿嘿～吃干抹净～♡♡ :: @fStikBot | 119 | 27,864,604 B |
| 33 | `LLM_Moe.json` | LLM小妹 | 120 | 37,246,095 B |
| 34 | `cd82afff_by_fStikBot.json` | [HAL♂] :: @fStikBot | 28 | 4,810,661 B |
| 35 | `zhiyong2.json` | 自用2 | 56 | 12,333,450 B |
| 36 | `KomeijiQualia.json` | 古明地歌の自用 | 55 | 12,610,477 B |
| 37 | `Shiroinu_shindoromu_By_LuoDian.json` | しろいぬシンドローム @LuoDian_Stickers | 86 | 17,054,227 B |
| 38 | `fuckyiyi.json` | 忆忆怪话集 | 114 | 12,828,940 B |
| 39 | `HanaCS2Video.json` | @HanaCS2 | 9 | 1,230,131 B |
| 40 | `ai_think_by_lolspbot.json` | Thinking | 13 | 290,901 B |
| 41 | `Unconscious_Apricot_Salamander_by_fStikBot.json` | 得卢，爱卢 :: @fStikBot | 16 | 3,460,314 B |
| 42 | `usagi_stickers.json` | 宇佐紀ノノ_usagi | 41 | 10,464,906 B |
| 43 | `realYoshino.json` | 自用 | 61 | 15,426,916 B |
| 44 | `inekokkk_by_fStikBot.json` | 𝔸𝕫𝕦𝕟𝕖𝕜𝕠 | 120 | 22,302,725 B |
| 45 | `line_220157684395_by_moe_sticker_bot.json` | ラブライブ！にじよん @moe_sticker_bot @Takius | 40 | 9,355,852 B |
| 46 | `WikiAbusers.json` | 滥权 | 120 | 16,413,321 B |
| 47 | `firefly_ek121_1_by_moe_sticker_bot.json` | 流萤小表情 \| Pixiv: ek121 | 69 | 18,822,814 B |
| 48 | `aic02.json` | AliceInCradle@Sakuraba_O | 52 | 13,870,245 B |
| 49 | `qi2_lu4_nuo4_by_fStikBot.json` | 琪露诺 | 120 | 25,723,985 B |
| 50 | `Sticker_Leaking_NEWW_by_fStikBot.json` | Sticker Leaking NEW :: @fStikBot | 65 | 7,977,734 B |
| 51 | `USABest.json` | USA best::@aerodynamic39 | 0 | 0 B |
| 52 | `Cosmic_Princess_Kaguya_Pack1.json` | @sticker_freehk 超かぐや姫！ Pack1 | 1 | 32,255 B |
| 53 | `kawaiikipfel_by_moe_sticker_bot.json` | kipfel \| by @xy_Stickers | 0 | 0 B |
| 54 | `MygoStickerByAsahiRise.json` | Mygo Sticker Twi:Asahi_rise | 0 | 0 B |
<!-- PACK_INDEX_END -->

## 四、各包逐張明細


## 1. `in_BCDGDC_by_NaiDrawBot` — `in_BCDGDC_by_NaiDrawBot.json`

- 標題:`in_BCDGDC_by_NaiDrawBot`;包 ID:`in_BCDGDC_by_NaiDrawBot`
- 張數:32;mimetype 分佈:image/png ×32
- 大小統計:合計 6,265,543 B(5.98 MB);平均 191.2 KB;最小 135.8 KB;最大 271.6 KB
- 來源 ID:sha256(外) ×32(全包皆為外部匯入條目)

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | in_BCDGDC_by_NaiDrawBot_10_👶.webp | image/png | 256x256 | 149.0 | sha256:63b15991936002f8…〔外〕 |
| 2 | in_BCDGDC_by_NaiDrawBot_11_🛩️.webp | image/png | 256x256 | 172.1 | sha256:6c6e3869bf46d6b9…〔外〕 |
| 3 | in_BCDGDC_by_NaiDrawBot_12_🚫.webp | image/png | 256x256 | 249.2 | sha256:47c7cd3b6d95c499…〔外〕 |
| 4 | in_BCDGDC_by_NaiDrawBot_13_😭.webp | image/png | 256x256 | 166.8 | sha256:d8b92f4be22f75dc…〔外〕 |
| 5 | in_BCDGDC_by_NaiDrawBot_14_👍.webp | image/png | 256x256 | 169.5 | sha256:ceb51eb859e07137…〔外〕 |
| 6 | in_BCDGDC_by_NaiDrawBot_15_❤️.webp | image/png | 256x256 | 157.6 | sha256:f78db3565a4358be…〔外〕 |
| 7 | in_BCDGDC_by_NaiDrawBot_16_📌.webp | image/png | 256x256 | 135.8 | sha256:2a17771a76e6df6b…〔外〕 |
| 8 | in_BCDGDC_by_NaiDrawBot_17_👀.webp | image/png | 256x256 | 211.8 | sha256:a2c7d53896521ec5…〔外〕 |
| 9 | in_BCDGDC_by_NaiDrawBot_18_❤️.webp | image/png | 256x256 | 204.4 | sha256:811d5709400a8192…〔外〕 |
| 10 | in_BCDGDC_by_NaiDrawBot_19_👍.webp | image/png | 256x256 | 219.6 | sha256:9d938d592d484266…〔外〕 |
| 11 | in_BCDGDC_by_NaiDrawBot_1_🚫.webp | image/png | 256x256 | 196.7 | sha256:048f4ae828eccaca…〔外〕 |
| 12 | in_BCDGDC_by_NaiDrawBot_20_😭.webp | image/png | 256x256 | 247.9 | sha256:ae7e9aae2f8e81f5…〔外〕 |
| 13 | in_BCDGDC_by_NaiDrawBot_21_🚫.webp | image/png | 256x256 | 240.4 | sha256:f8b4374809b2f7de…〔外〕 |
| 14 | in_BCDGDC_by_NaiDrawBot_22_👉.webp | image/png | 256x256 | 215.2 | sha256:170527ead36cff94…〔外〕 |
| 15 | in_BCDGDC_by_NaiDrawBot_23_🚪.webp | image/png | 256x256 | 196.2 | sha256:5d60a8fb2b6054fb…〔外〕 |
| 16 | in_BCDGDC_by_NaiDrawBot_24_❤️.webp | image/png | 256x256 | 198.7 | sha256:6d75c45d622f8825…〔外〕 |
| 17 | in_BCDGDC_by_NaiDrawBot_25_🤚.webp | image/png | 256x256 | 221.8 | sha256:4920fc9fe321670b…〔外〕 |
| 18 | in_BCDGDC_by_NaiDrawBot_26_❤️.webp | image/png | 256x256 | 238.6 | sha256:29d27931adef0cba…〔外〕 |
| 19 | in_BCDGDC_by_NaiDrawBot_27_🏠.webp | image/png | 256x256 | 213.1 | sha256:7f713c52d060c822…〔外〕 |
| 20 | in_BCDGDC_by_NaiDrawBot_28_🚫.webp | image/png | 256x256 | 208.6 | sha256:96a31b2cf1802fe9…〔外〕 |
| 21 | in_BCDGDC_by_NaiDrawBot_29_🤗.webp | image/png | 256x256 | 206.4 | sha256:f591972585f461a0…〔外〕 |
| 22 | in_BCDGDC_by_NaiDrawBot_2_👍.webp | image/png | 256x256 | 177.9 | sha256:780d119cccac2b67…〔外〕 |
| 23 | in_BCDGDC_by_NaiDrawBot_30_🦊.webp | image/png | 256x256 | 204.8 | sha256:56946ff672f60206…〔外〕 |
| 24 | in_BCDGDC_by_NaiDrawBot_31_😮.webp | image/png | 256x256 | 210.4 | sha256:e9b8a131a395aa4c…〔外〕 |
| 25 | in_BCDGDC_by_NaiDrawBot_32_🤗.webp | image/png | 256x256 | 271.6 | sha256:02888cc5de27d66c…〔外〕 |
| 26 | in_BCDGDC_by_NaiDrawBot_3_👧.webp | image/png | 256x256 | 153.4 | sha256:12901fe045a14456…〔外〕 |
| 27 | in_BCDGDC_by_NaiDrawBot_4_😭.webp | image/png | 256x256 | 144.6 | sha256:91c7bd4e56b245f3…〔外〕 |
| 28 | in_BCDGDC_by_NaiDrawBot_5_😳.webp | image/png | 256x256 | 139.7 | sha256:66a4e9dfcd27588b…〔外〕 |
| 29 | in_BCDGDC_by_NaiDrawBot_6_🚫.webp | image/png | 256x256 | 150.2 | sha256:7a8dd294572ce472…〔外〕 |
| 30 | in_BCDGDC_by_NaiDrawBot_7_🤤.webp | image/png | 256x256 | 151.1 | sha256:68695c6dfb32446d…〔外〕 |
| 31 | in_BCDGDC_by_NaiDrawBot_8_👍.webp | image/png | 256x256 | 138.5 | sha256:a6889e17ab243d0f…〔外〕 |
| 32 | in_BCDGDC_by_NaiDrawBot_9_❤️.webp | image/png | 256x256 | 157.2 | sha256:11d2469632c63989…〔外〕 |


## 2. `ukuku1_2` — `ukuku1_2.json`

- 標題:`ukuku1_2`;包 ID:`ukuku1_2`
- 張數:45;mimetype 分佈:image/png ×45
- 大小統計:合計 7,930,657 B(7.56 MB);平均 172.1 KB;最小 97.6 KB;最大 204.0 KB
- 來源 ID:sha256(外) ×45(全包皆為外部匯入條目)

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | ukuku1_2_10_🥶.webp | image/png | 256x256 | 183.1 | sha256:79ab6844d8bf2031…〔外〕 |
| 2 | ukuku1_2_11_😠.webp | image/png | 256x256 | 179.9 | sha256:b8224deaa45ecba6…〔外〕 |
| 3 | ukuku1_2_12_🤤.webp | image/png | 256x256 | 163.4 | sha256:0bb7d9e537a53e96…〔外〕 |
| 4 | ukuku1_2_13_😨.webp | image/png | 256x256 | 181.3 | sha256:b2f7ff21ac0ac1c9…〔外〕 |
| 5 | ukuku1_2_14_😍.webp | image/png | 256x256 | 204.0 | sha256:e14433075ef37ea2…〔外〕 |
| 6 | ukuku1_2_15_☺️.webp | image/png | 256x256 | 187.5 | sha256:3ba61200437b28b7…〔外〕 |
| 7 | ukuku1_2_16_☺️.webp | image/png | 256x256 | 187.8 | sha256:bfd055378b199804…〔外〕 |
| 8 | ukuku1_2_17_😢.webp | image/png | 256x256 | 159.9 | sha256:4edbe0cc69353fcf…〔外〕 |
| 9 | ukuku1_2_18_😶.webp | image/png | 256x256 | 150.1 | sha256:0f142d446c686180…〔外〕 |
| 10 | ukuku1_2_19_😶.webp | image/png | 256x256 | 192.3 | sha256:baed5f1ecbb3d45e…〔外〕 |
| 11 | ukuku1_2_1_😊.webp | image/png | 256x256 | 184.5 | sha256:db275ed9dd539ce3…〔外〕 |
| 12 | ukuku1_2_20_☕️.webp | image/png | 256x256 | 184.8 | sha256:04c1f093e4ef9acf…〔外〕 |
| 13 | ukuku1_2_21_😭.webp | image/png | 256x256 | 169.3 | sha256:456b9ccf5a478157…〔外〕 |
| 14 | ukuku1_2_22_😐.webp | image/png | 256x256 | 182.2 | sha256:93ceacf7c53d457d…〔外〕 |
| 15 | ukuku1_2_23_😈.webp | image/png | 256x256 | 180.6 | sha256:d250572c43d1dd1d…〔外〕 |
| 16 | ukuku1_2_24_🤗.webp | image/png | 256x256 | 188.1 | sha256:c104593e72e199c2…〔外〕 |
| 17 | ukuku1_2_25_🤔.webp | image/png | 256x256 | 165.7 | sha256:45374f7ef3218be5…〔外〕 |
| 18 | ukuku1_2_26_😷.webp | image/png | 256x256 | 146.8 | sha256:9e5b4fb2e683db43…〔外〕 |
| 19 | ukuku1_2_27_☺️.webp | image/png | 256x256 | 164.6 | sha256:b56dc88b47ad1c24…〔外〕 |
| 20 | ukuku1_2_28_😵.webp | image/png | 256x256 | 181.7 | sha256:d66c50d5bbafe7d9…〔外〕 |
| 21 | ukuku1_2_29_😨.webp | image/png | 256x256 | 150.5 | sha256:ca5b866b3a6e6724…〔外〕 |
| 22 | ukuku1_2_2_❗️.webp | image/png | 256x256 | 115.7 | sha256:edabd00e3268c9bf…〔外〕 |
| 23 | ukuku1_2_30_😫.webp | image/png | 256x256 | 167.2 | sha256:e28de85805b7e8ed…〔外〕 |
| 24 | ukuku1_2_31_🤕.webp | image/png | 256x256 | 201.9 | sha256:a1568d8923974070…〔外〕 |
| 25 | ukuku1_2_32_🍦.webp | image/png | 256x256 | 164.1 | sha256:46b3067e5737e4a4…〔外〕 |
| 26 | ukuku1_2_33_🔫.webp | image/png | 256x256 | 154.2 | sha256:2bbac19c1d863c4d…〔外〕 |
| 27 | ukuku1_2_34_😏.webp | image/png | 256x256 | 198.7 | sha256:8c6e242812dcc261…〔外〕 |
| 28 | ukuku1_2_35_😏.webp | image/png | 256x256 | 184.2 | sha256:a3a33ba6b3e4790d…〔外〕 |
| 29 | ukuku1_2_36_☝️.webp | image/png | 256x256 | 170.8 | sha256:6cd77cafe7c9c3ff…〔外〕 |
| 30 | ukuku1_2_37_😖.webp | image/png | 256x256 | 172.1 | sha256:42f9594a0d43c40d…〔外〕 |
| 31 | ukuku1_2_38_😣.webp | image/png | 256x256 | 187.1 | sha256:b80334340623060d…〔外〕 |
| 32 | ukuku1_2_39_😪.webp | image/png | 256x256 | 194.3 | sha256:586058505159ef6a…〔外〕 |
| 33 | ukuku1_2_3_🤨.webp | image/png | 256x256 | 201.4 | sha256:4486cb4517a478ff…〔外〕 |
| 34 | ukuku1_2_40_😐.webp | image/png | 256x256 | 184.2 | sha256:afc277fa0c107bc5…〔外〕 |
| 35 | ukuku1_2_41_😌.webp | image/png | 256x256 | 161.7 | sha256:e02547ad3f95396a…〔外〕 |
| 36 | ukuku1_2_42_🍉.webp | image/png | 256x256 | 183.8 | sha256:3524be1a5b89084e…〔外〕 |
| 37 | ukuku1_2_43_🥱.webp | image/png | 256x256 | 145.4 | sha256:41ee41344909dcc3…〔外〕 |
| 38 | ukuku1_2_44_😶.webp | image/png | 256x256 | 97.6 | sha256:67de3b53e697b356…〔外〕 |
| 39 | ukuku1_2_45_💢.webp | image/png | 256x256 | 166.4 | sha256:214180cca4a783b3…〔外〕 |
| 40 | ukuku1_2_4_❓.webp | image/png | 256x256 | 171.4 | sha256:b6e6723cc95d8037…〔外〕 |
| 41 | ukuku1_2_5_📘.webp | image/png | 256x256 | 177.9 | sha256:b7741c3017d59504…〔外〕 |
| 42 | ukuku1_2_6_🤮.webp | image/png | 256x256 | 139.2 | sha256:b27c48e11c64f4e6…〔外〕 |
| 43 | ukuku1_2_7_🥱.webp | image/png | 256x256 | 188.1 | sha256:9910382647725c6d…〔外〕 |
| 44 | ukuku1_2_8_😘.webp | image/png | 256x256 | 180.5 | sha256:451983a1d77d6815…〔外〕 |
| 45 | ukuku1_2_9_😣.webp | image/png | 256x256 | 148.9 | sha256:e86502edc503bc7f…〔外〕 |


## 3. `ArcaeaLinkPlay` — `ArcaeaLinkPlay.json`

- 標題:`ArcaeaLinkPlay`;包 ID:`ArcaeaLinkPlay`
- 張數:46;mimetype 分佈:image/png ×46
- 大小統計:合計 14,049,408 B(13.40 MB);平均 298.3 KB;最小 230.8 KB;最大 346.5 KB
- 來源 ID:sha256(外) ×46(全包皆為外部匯入條目)

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | ArcaeaLinkPlay_10_👍.webp | image/png | 256x256 | 315.8 | sha256:3961ec1abc60d0b8…〔外〕 |
| 2 | ArcaeaLinkPlay_11_👍.webp | image/png | 256x256 | 336.9 | sha256:21fcc750ef372157…〔外〕 |
| 3 | ArcaeaLinkPlay_12_👍.webp | image/png | 256x256 | 346.5 | sha256:9376db3af6fc703e…〔外〕 |
| 4 | ArcaeaLinkPlay_13_👍.webp | image/png | 256x256 | 328.0 | sha256:8098d4c6449a834a…〔外〕 |
| 5 | ArcaeaLinkPlay_14_👍.webp | image/png | 256x256 | 327.2 | sha256:99380e3a7ec62ace…〔外〕 |
| 6 | ArcaeaLinkPlay_15_❤️.webp | image/png | 256x256 | 297.7 | sha256:28e05e839fcc2a55…〔外〕 |
| 7 | ArcaeaLinkPlay_16_❤️.webp | image/png | 256x256 | 298.9 | sha256:e942729a1f6692e4…〔外〕 |
| 8 | ArcaeaLinkPlay_17_❤️.webp | image/png | 256x256 | 305.0 | sha256:8226e879606f18b2…〔外〕 |
| 9 | ArcaeaLinkPlay_18_❤️.webp | image/png | 256x256 | 305.2 | sha256:da28925ca31f5ea4…〔外〕 |
| 10 | ArcaeaLinkPlay_19_🤔.webp | image/png | 256x256 | 313.8 | sha256:e067d94619ea52b8…〔外〕 |
| 11 | ArcaeaLinkPlay_1_😀.webp | image/png | 256x256 | 272.2 | sha256:bbcbebc838a5e3dd…〔外〕 |
| 12 | ArcaeaLinkPlay_20_🤔.webp | image/png | 256x256 | 336.7 | sha256:b8009c0dbf98db5e…〔外〕 |
| 13 | ArcaeaLinkPlay_21_🤔.webp | image/png | 256x256 | 321.2 | sha256:63e307ff82ef7790…〔外〕 |
| 14 | ArcaeaLinkPlay_22_🤔.webp | image/png | 256x256 | 325.1 | sha256:b8dce026690fcd04…〔外〕 |
| 15 | ArcaeaLinkPlay_23_🤔.webp | image/png | 256x256 | 328.8 | sha256:99446186bd5297aa…〔外〕 |
| 16 | ArcaeaLinkPlay_24_😎.webp | image/png | 256x256 | 285.7 | sha256:dce9d724a586877f…〔外〕 |
| 17 | ArcaeaLinkPlay_25_😎.webp | image/png | 256x256 | 292.6 | sha256:719f9e271adb61ff…〔外〕 |
| 18 | ArcaeaLinkPlay_26_😎.webp | image/png | 256x256 | 279.7 | sha256:e9bc836d3b22f6dd…〔外〕 |
| 19 | ArcaeaLinkPlay_27_😎.webp | image/png | 256x256 | 285.7 | sha256:d7d8478a71a6dece…〔外〕 |
| 20 | ArcaeaLinkPlay_28_😣.webp | image/png | 256x256 | 279.5 | sha256:add0d9ccb430bdbd…〔外〕 |
| 21 | ArcaeaLinkPlay_29_😨.webp | image/png | 256x256 | 296.6 | sha256:b91993eb3323bb15…〔外〕 |
| 22 | ArcaeaLinkPlay_2_😉.webp | image/png | 256x256 | 312.8 | sha256:73ebbcc48b45309e…〔外〕 |
| 23 | ArcaeaLinkPlay_30_😨.webp | image/png | 256x256 | 291.2 | sha256:3ccc2f494bdeab8d…〔外〕 |
| 24 | ArcaeaLinkPlay_31_😨.webp | image/png | 256x256 | 294.9 | sha256:e59ab930bbc0fdf1…〔外〕 |
| 25 | ArcaeaLinkPlay_32_😨.webp | image/png | 256x256 | 296.6 | sha256:5b6b49f240e1075c…〔外〕 |
| 26 | ArcaeaLinkPlay_33_☺️.webp | image/png | 256x256 | 282.2 | sha256:2c7243ea4e84cabc…〔外〕 |
| 27 | ArcaeaLinkPlay_34_☺️.webp | image/png | 256x256 | 282.9 | sha256:dc7b5bf882866390…〔外〕 |
| 28 | ArcaeaLinkPlay_35_☺️.webp | image/png | 256x256 | 282.9 | sha256:874c09a03ec27d66…〔外〕 |
| 29 | ArcaeaLinkPlay_36_☺️.webp | image/png | 256x256 | 284.9 | sha256:ce73dffb7d730788…〔外〕 |
| 30 | ArcaeaLinkPlay_37_☺️.webp | image/png | 256x256 | 285.4 | sha256:1ee0c6f831a5b4c5…〔外〕 |
| 31 | ArcaeaLinkPlay_38_👆.webp | image/png | 256x256 | 290.5 | sha256:528a46051f15dc47…〔外〕 |
| 32 | ArcaeaLinkPlay_39_👆.webp | image/png | 256x256 | 299.2 | sha256:9cdc26bcd3571764…〔外〕 |
| 33 | ArcaeaLinkPlay_3_😉.webp | image/png | 256x256 | 325.2 | sha256:3421b53fb1d52a28…〔外〕 |
| 34 | ArcaeaLinkPlay_40_👆.webp | image/png | 256x256 | 300.2 | sha256:17d9115b398604f0…〔外〕 |
| 35 | ArcaeaLinkPlay_41_👆.webp | image/png | 256x256 | 285.7 | sha256:49251e0076896dd1…〔外〕 |
| 36 | ArcaeaLinkPlay_42_👆.webp | image/png | 256x256 | 289.0 | sha256:47514da88a1d083e…〔外〕 |
| 37 | ArcaeaLinkPlay_43_👌.webp | image/png | 256x256 | 230.8 | sha256:42b1d202890da764…〔外〕 |
| 38 | ArcaeaLinkPlay_44_👌.webp | image/png | 256x256 | 235.6 | sha256:06838a3457b89a1d…〔外〕 |
| 39 | ArcaeaLinkPlay_45_👌.webp | image/png | 256x256 | 242.9 | sha256:d1183216d7616b72…〔外〕 |
| 40 | ArcaeaLinkPlay_46_👌.webp | image/png | 256x256 | 244.0 | sha256:82caa67e29064d45…〔外〕 |
| 41 | ArcaeaLinkPlay_4_😉.webp | image/png | 256x256 | 321.8 | sha256:e551d0e5a2bc2c92…〔外〕 |
| 42 | ArcaeaLinkPlay_5_😉.webp | image/png | 256x256 | 328.2 | sha256:5940c176ed98cf47…〔外〕 |
| 43 | ArcaeaLinkPlay_6_😀.webp | image/png | 256x256 | 308.2 | sha256:56920bd47a94be39…〔外〕 |
| 44 | ArcaeaLinkPlay_7_😀.webp | image/png | 256x256 | 310.9 | sha256:d6fd5ec9fcb4f0f2…〔外〕 |
| 45 | ArcaeaLinkPlay_8_😀.webp | image/png | 256x256 | 308.4 | sha256:de5c8d457fb657b2…〔外〕 |
| 46 | ArcaeaLinkPlay_9_😀.webp | image/png | 256x256 | 306.7 | sha256:3fa5729d204148d4…〔外〕 |


## 4. `Archwizard_pack` — `Archwizard_pack.json`

- 標題:`Archwizard_pack`;包 ID:`Archwizard_pack`
- 張數:69;mimetype 分佈:image/png ×69
- 大小統計:合計 14,562,911 B(13.89 MB);平均 206.1 KB;最小 26.2 KB;最大 371.5 KB
- 來源 ID:sha256(外) ×69(全包皆為外部匯入條目)

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | Archwizard_pack_10_🖕.webp | image/png | 256x168 | 278.7 | sha256:d68ca51d2332ca24…〔外〕 |
| 2 | Archwizard_pack_11_😯.webp | image/png | 256x125 | 61.5 | sha256:df4d909d7e6fa2e1…〔外〕 |
| 3 | Archwizard_pack_12_✋.webp | image/png | 256x177 | 278.9 | sha256:50395cbe317c5358…〔外〕 |
| 4 | Archwizard_pack_13_👎.webp | image/png | 256x175 | 271.9 | sha256:99b75d28957f7b38…〔外〕 |
| 5 | Archwizard_pack_14_❓.webp | image/png | 256x249 | 293.2 | sha256:d2f5f3dedc3dddf4…〔外〕 |
| 6 | Archwizard_pack_15_🙉.webp | image/png | 256x190 | 169.2 | sha256:e8cde53a69ade0f1…〔外〕 |
| 7 | Archwizard_pack_16_😭.webp | image/png | 256x256 | 172.1 | sha256:a41f21d936314fd0…〔外〕 |
| 8 | Archwizard_pack_17_🔫.webp | image/png | 256x246 | 308.0 | sha256:788f1eb39d050492…〔外〕 |
| 9 | Archwizard_pack_18_💢.webp | image/png | 256x144 | 251.2 | sha256:fff2831cbeb4215c…〔外〕 |
| 10 | Archwizard_pack_19_🤩.webp | image/png | 256x145 | 238.7 | sha256:e129f4dddcf31a03…〔外〕 |
| 11 | Archwizard_pack_1_👋.webp | image/png | 256x248 | 269.5 | sha256:b271cd74a2711615…〔外〕 |
| 12 | Archwizard_pack_20_👀.webp | image/png | 256x144 | 327.7 | sha256:e749cb348877e23c…〔外〕 |
| 13 | Archwizard_pack_21_😫.webp | image/png | 256x231 | 117.1 | sha256:1553d1ada2d14718…〔外〕 |
| 14 | Archwizard_pack_22_😾.webp | image/png | 256x256 | 189.7 | sha256:3bb159b9c0f295c8…〔外〕 |
| 15 | Archwizard_pack_23_😖.webp | image/png | 256x217 | 104.5 | sha256:13b8735f0ad0c1e1…〔外〕 |
| 16 | Archwizard_pack_24_🙄.webp | image/png | 233x256 | 243.5 | sha256:df871fa5bc3ddd20…〔外〕 |
| 17 | Archwizard_pack_25_🧐.webp | image/png | 256x221 | 161.0 | sha256:beb77fbeaedcaabe…〔外〕 |
| 18 | Archwizard_pack_26_❓.webp | image/png | 214x256 | 194.1 | sha256:daa7357118775022…〔外〕 |
| 19 | Archwizard_pack_27_👌.webp | image/png | 256x221 | 173.8 | sha256:94194b07ce4721eb…〔外〕 |
| 20 | Archwizard_pack_28_🌿.webp | image/png | 256x256 | 111.2 | sha256:a20a4bab2962038e…〔外〕 |
| 21 | Archwizard_pack_29_📈.webp | image/png | 256x256 | 132.8 | sha256:f662730bc112f845…〔外〕 |
| 22 | Archwizard_pack_2_👽.webp | image/png | 256x255 | 207.6 | sha256:122679cee5a6e151…〔外〕 |
| 23 | Archwizard_pack_30_📈.webp | image/png | 256x256 | 160.0 | sha256:c6b5b80c3cd1d5b9…〔外〕 |
| 24 | Archwizard_pack_31_📉.webp | image/png | 256x256 | 132.9 | sha256:ece5aae7e0046cf3…〔外〕 |
| 25 | Archwizard_pack_32_⚰️.webp | image/png | 256x256 | 99.9 | sha256:0a36cc5d3b53ccbb…〔外〕 |
| 26 | Archwizard_pack_33_😤.webp | image/png | 256x256 | 353.2 | sha256:59b30aa540a73b04…〔外〕 |
| 27 | Archwizard_pack_34_🙀.webp | image/png | 256x256 | 226.7 | sha256:f8d808f6abc9da4a…〔外〕 |
| 28 | Archwizard_pack_35_💸.webp | image/png | 256x247 | 371.5 | sha256:1390db99fb095d6e…〔外〕 |
| 29 | Archwizard_pack_36_☕️.webp | image/png | 256x164 | 148.9 | sha256:690d14c5156cd2a8…〔外〕 |
| 30 | Archwizard_pack_37_😾.webp | image/png | 256x201 | 229.0 | sha256:09f3d5fdbe88e000…〔外〕 |
| 31 | Archwizard_pack_38_5️⃣.webp | image/png | 256x208 | 61.1 | sha256:1163e1946a6cee84…〔外〕 |
| 32 | Archwizard_pack_39_👍.webp | image/png | 256x198 | 196.2 | sha256:e14af9815cba22b3…〔外〕 |
| 33 | Archwizard_pack_3_😆.webp | image/png | 256x256 | 368.8 | sha256:e0ccb640934abe96…〔外〕 |
| 34 | Archwizard_pack_40_😫.webp | image/png | 256x256 | 173.9 | sha256:fd6872a2aed3cfdd…〔外〕 |
| 35 | Archwizard_pack_41_👀.webp | image/png | 256x48 | 87.6 | sha256:d0c75fd2dce51cf3…〔外〕 |
| 36 | Archwizard_pack_42_😅.webp | image/png | 179x256 | 203.6 | sha256:d74247bf8f0770a5…〔外〕 |
| 37 | Archwizard_pack_43_⚡️.webp | image/png | 256x103 | 91.7 | sha256:6bc91b0e09119a7a…〔外〕 |
| 38 | Archwizard_pack_44_😭.webp | image/png | 256x253 | 286.9 | sha256:41a3f2e522f8e13c…〔外〕 |
| 39 | Archwizard_pack_45_😔.webp | image/png | 256x256 | 289.8 | sha256:bdd133138c718ca5…〔外〕 |
| 40 | Archwizard_pack_46_😝.webp | image/png | 255x256 | 277.8 | sha256:e3e1a1105dd3bdf6…〔外〕 |
| 41 | Archwizard_pack_47_🥺.webp | image/png | 256x256 | 91.7 | sha256:f9e5e9c46448d5b6…〔外〕 |
| 42 | Archwizard_pack_48_💀.webp | image/png | 256x256 | 26.2 | sha256:aff5259bb543d8e5…〔外〕 |
| 43 | Archwizard_pack_49_🙁.webp | image/png | 218x256 | 203.3 | sha256:b323b45ae7b06eb1…〔外〕 |
| 44 | Archwizard_pack_4_😵.webp | image/png | 202x256 | 92.5 | sha256:e47d8596925d7383…〔外〕 |
| 45 | Archwizard_pack_50_❓.webp | image/png | 248x256 | 240.6 | sha256:8493bacb21ba2db2…〔外〕 |
| 46 | Archwizard_pack_51_😧.webp | image/png | 256x251 | 184.4 | sha256:96b21fac58a9cf81…〔外〕 |
| 47 | Archwizard_pack_52_⭐️.webp | image/png | 256x231 | 129.0 | sha256:53f72a9df4fd8499…〔外〕 |
| 48 | Archwizard_pack_53_👍.webp | image/png | 256x256 | 143.8 | sha256:a0b281c9bfb3d6de…〔外〕 |
| 49 | Archwizard_pack_54_🧏‍♂️.webp | image/png | 256x178 | 117.7 | sha256:83a597cab7ac9777…〔外〕 |
| 50 | Archwizard_pack_55_🏃.webp | image/png | 256x186 | 262.9 | sha256:1f19c18d84e3310a…〔外〕 |
| 51 | Archwizard_pack_56_🤷.webp | image/png | 256x221 | 130.3 | sha256:ea977d754713dc84…〔外〕 |
| 52 | Archwizard_pack_57_😑.webp | image/png | 229x256 | 329.9 | sha256:663889c2bb15a05d…〔外〕 |
| 53 | Archwizard_pack_58_🤔.webp | image/png | 256x239 | 291.7 | sha256:11831087b140f10f…〔外〕 |
| 54 | Archwizard_pack_59_🖌.webp | image/png | 256x221 | 263.9 | sha256:9670b9f56aa282f9…〔外〕 |
| 55 | Archwizard_pack_5_😶.webp | image/png | 256x256 | 276.3 | sha256:cdec1d3879dcb155…〔外〕 |
| 56 | Archwizard_pack_60_🖌.webp | image/png | 256x221 | 259.9 | sha256:6c8de09c3d12908c…〔外〕 |
| 57 | Archwizard_pack_61_🃏.webp | image/png | 176x256 | 223.3 | sha256:73a20dbf09f97bd4…〔外〕 |
| 58 | Archwizard_pack_62_😁.webp | image/png | 256x192 | 236.2 | sha256:9253b86d7ae6b487…〔外〕 |
| 59 | Archwizard_pack_63_🐭.webp | image/png | 255x256 | 248.8 | sha256:9016cede7a8acdd2…〔外〕 |
| 60 | Archwizard_pack_64_🌿.webp | image/png | 256x225 | 177.8 | sha256:aaa874f53e4667b5…〔外〕 |
| 61 | Archwizard_pack_65_🤗.webp | image/png | 245x256 | 216.8 | sha256:0b4804d3048fdb9a…〔外〕 |
| 62 | Archwizard_pack_66_💣.webp | image/png | 256x256 | 157.6 | sha256:828cb6ee565cfd25…〔外〕 |
| 63 | Archwizard_pack_67_❓.webp | image/png | 212x256 | 186.9 | sha256:685d7f341994cc5d…〔外〕 |
| 64 | Archwizard_pack_68_🙀.webp | image/png | 256x144 | 126.5 | sha256:116f1fe8a8d8572f…〔外〕 |
| 65 | Archwizard_pack_69_😭.webp | image/png | 256x233 | 273.6 | sha256:50429e776e6d8cb4…〔外〕 |
| 66 | Archwizard_pack_6_😒.webp | image/png | 256x256 | 252.2 | sha256:24e9384e4adbda4f…〔外〕 |
| 67 | Archwizard_pack_7_🫠.webp | image/png | 256x240 | 281.0 | sha256:d9beafa0e90b682c…〔外〕 |
| 68 | Archwizard_pack_8_😏.webp | image/png | 256x256 | 260.5 | sha256:7807078b7f37ce84…〔外〕 |
| 69 | Archwizard_pack_9_🤠.webp | image/png | 256x256 | 220.9 | sha256:96fdb7873aff261f…〔外〕 |


## 5. `CacheCI` — `CacheCI.json`

- 標題:`CacheCI`;包 ID:`CacheCI`
- 張數:107;mimetype 分佈:image/png ×107
- 大小統計:合計 20,473,338 B(19.52 MB);平均 186.9 KB;最小 2.1 KB;最大 704.6 KB
- 來源 ID:sha256(外) ×107(全包皆為外部匯入條目)

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | CacheCI_100_😡.webp | image/png | 256x153 | 59.8 | sha256:20c15be0064950fb…〔外〕 |
| 2 | CacheCI_101_💾.webp | image/png | 199x256 | 299.7 | sha256:81a5fc5b2e2d4422…〔外〕 |
| 3 | CacheCI_102_⭐️.webp | image/png | 170x256 | 135.2 | sha256:772bc3d4af568d78…〔外〕 |
| 4 | CacheCI_103_🗑.webp | image/png | 256x256 | 281.9 | sha256:6c2a222e3b463850…〔外〕 |
| 5 | CacheCI_104_🤓.webp | image/png | 256x256 | 157.3 | sha256:2715705b703ee4f4…〔外〕 |
| 6 | CacheCI_105_☝️.webp | image/png | 244x256 | 268.3 | sha256:2dc007a07ae082d6…〔外〕 |
| 7 | CacheCI_106_👊.webp | image/png | 256x234 | 167.9 | sha256:eb50a9efea844929…〔外〕 |
| 8 | CacheCI_107_💸.webp | image/png | 233x256 | 107.0 | sha256:f2055b696fbcc36e…〔外〕 |
| 9 | CacheCI_10_😀.webp | image/png | 256x256 | 174.6 | sha256:0803b189a6f81e56…〔外〕 |
| 10 | CacheCI_11_🔪.webp | image/png | 256x256 | 291.1 | sha256:f897315c13eec31c…〔外〕 |
| 11 | CacheCI_12_😕.webp | image/png | 256x256 | 61.5 | sha256:14c65a80e9019abd…〔外〕 |
| 12 | CacheCI_13_😂.webp | image/png | 211x256 | 183.1 | sha256:381eb191898d05a6…〔外〕 |
| 13 | CacheCI_14_👃.webp | image/png | 256x160 | 211.9 | sha256:67e76287baea671e…〔外〕 |
| 14 | CacheCI_15_🚫.webp | image/png | 256x196 | 99.3 | sha256:3915d4f07043dd7c…〔外〕 |
| 15 | CacheCI_16_😢.webp | image/png | 256x256 | 172.0 | sha256:a4336d57ca4d11b2…〔外〕 |
| 16 | CacheCI_17_💢.webp | image/png | 256x256 | 211.8 | sha256:46829bc447e40176…〔外〕 |
| 17 | CacheCI_18_🤔.webp | image/png | 228x256 | 54.1 | sha256:d273088ae4388cc4…〔外〕 |
| 18 | CacheCI_19_📝.webp | image/png | 256x256 | 185.5 | sha256:41999ee8042f3800…〔外〕 |
| 19 | CacheCI_1_🏃.webp | image/png | 256x196 | 142.1 | sha256:29500988273b5f4b…〔外〕 |
| 20 | CacheCI_20_📦.webp | image/png | 250x256 | 258.7 | sha256:000592b9106eb64d…〔外〕 |
| 21 | CacheCI_21_👍.webp | image/png | 256x256 | 239.3 | sha256:4951da9a42ff5bbf…〔外〕 |
| 22 | CacheCI_22_🪙.webp | image/png | 192x256 | 272.2 | sha256:04c634557758b26e…〔外〕 |
| 23 | CacheCI_23_😵.webp | image/png | 249x256 | 383.2 | sha256:8093347c2e761ab5…〔外〕 |
| 24 | CacheCI_24_💭.webp | image/png | 256x234 | 242.5 | sha256:12664343618c3f88…〔外〕 |
| 25 | CacheCI_25_🧠.webp | image/png | 256x256 | 155.0 | sha256:316230911c5f5e4e…〔外〕 |
| 26 | CacheCI_26_😵.webp | image/png | 256x189 | 211.0 | sha256:ac50c042d5b77d04…〔外〕 |
| 27 | CacheCI_27_👎.webp | image/png | 256x185 | 251.7 | sha256:5964718a010e2ab8…〔外〕 |
| 28 | CacheCI_28_👎.webp | image/png | 256x244 | 310.7 | sha256:ae9b79ce082cea60…〔外〕 |
| 29 | CacheCI_29_👍.webp | image/png | 229x256 | 246.4 | sha256:208cd5f9db74149f…〔外〕 |
| 30 | CacheCI_2_👎.webp | image/png | 256x256 | 79.0 | sha256:ae2df8b70971510a…〔外〕 |
| 31 | CacheCI_30_😅.webp | image/png | 256x256 | 81.0 | sha256:7e2c1883fd4a1354…〔外〕 |
| 32 | CacheCI_31_😳.webp | image/png | 256x256 | 98.9 | sha256:f9b466a2c299f409…〔外〕 |
| 33 | CacheCI_32_😭.webp | image/png | 256x256 | 230.8 | sha256:eab8314b83fc6399…〔外〕 |
| 34 | CacheCI_33_🗡.webp | image/png | 256x251 | 209.4 | sha256:ac00331d1fde96e2…〔外〕 |
| 35 | CacheCI_34_😶.webp | image/png | 256x121 | 93.9 | sha256:8bfd96ae0f5179fe…〔外〕 |
| 36 | CacheCI_35_😁.webp | image/png | 256x126 | 104.2 | sha256:9f1c3cff74d2b984…〔外〕 |
| 37 | CacheCI_36_👉.webp | image/png | 249x256 | 123.0 | sha256:4255fe0d53374d01…〔外〕 |
| 38 | CacheCI_37_🦸.webp | image/png | 256x159 | 218.8 | sha256:46c07a9ec2fd68a4…〔外〕 |
| 39 | CacheCI_38_👎.webp | image/png | 256x233 | 108.0 | sha256:a323ade0b48c252a…〔外〕 |
| 40 | CacheCI_39_👍.webp | image/png | 256x225 | 100.9 | sha256:bd94159194d1a412…〔外〕 |
| 41 | CacheCI_3_☘.webp | image/png | 256x69 | 48.8 | sha256:ba8c53f2c4d0af59…〔外〕 |
| 42 | CacheCI_40_💊.webp | image/png | 158x256 | 150.6 | sha256:aa8296597e37a3c5…〔外〕 |
| 43 | CacheCI_41_⚰.webp | image/png | 256x256 | 423.7 | sha256:2f40f830dc69a1cd…〔外〕 |
| 44 | CacheCI_42_✔.webp | image/png | 256x256 | 303.0 | sha256:2e84c2c361f6292a…〔外〕 |
| 45 | CacheCI_43_🤬.webp | image/png | 256x253 | 183.8 | sha256:4fe1e1481858c3e1…〔外〕 |
| 46 | CacheCI_44_💊.webp | image/png | 256x215 | 132.7 | sha256:2db79a5022f1e950…〔外〕 |
| 47 | CacheCI_45_👀.webp | image/png | 256x145 | 106.1 | sha256:b3d4e24a610a3772…〔外〕 |
| 48 | CacheCI_46_📸.webp | image/png | 256x244 | 210.3 | sha256:03e711214345e337…〔外〕 |
| 49 | CacheCI_47_😍.webp | image/png | 256x256 | 305.1 | sha256:77848209c7bba2c8…〔外〕 |
| 50 | CacheCI_48_🎧.webp | image/png | 256x256 | 206.1 | sha256:c08c8330d7a36e78…〔外〕 |
| 51 | CacheCI_49_💯.webp | image/png | 256x183 | 75.8 | sha256:89e90ff4d343cbbb…〔外〕 |
| 52 | CacheCI_4_👎.webp | image/png | 211x256 | 158.2 | sha256:b429bac47208d63f…〔外〕 |
| 53 | CacheCI_50_🖼.webp | image/png | 256x229 | 257.4 | sha256:8766d3f59985b055…〔外〕 |
| 54 | CacheCI_51_💾.webp | image/png | 256x182 | 200.6 | sha256:5f6fbc97adbb8134…〔外〕 |
| 55 | CacheCI_52_🖼.webp | image/png | 256x184 | 235.8 | sha256:4b96db28e71e23c0…〔外〕 |
| 56 | CacheCI_53_😐.webp | image/png | 256x256 | 177.5 | sha256:6cf740f06a967730…〔外〕 |
| 57 | CacheCI_54_😹.webp | image/png | 256x240 | 133.5 | sha256:9110985a26b06448…〔外〕 |
| 58 | CacheCI_55_🖕.webp | image/png | 256x256 | 217.4 | sha256:7212cf623c9aa1b7…〔外〕 |
| 59 | CacheCI_56_🐉.webp | image/png | 192x256 | 202.8 | sha256:28cd0f5d4c9788aa…〔外〕 |
| 60 | CacheCI_57_👎.webp | image/png | 256x145 | 199.4 | sha256:f1419defa714664f…〔外〕 |
| 61 | CacheCI_58_🤔.webp | image/png | 256x256 | 6.1 | sha256:bd1b0c0fbae5f902…〔外〕 |
| 62 | CacheCI_59_🌿.webp | image/png | 256x256 | 62.4 | sha256:67e65b0c1665d7f3…〔外〕 |
| 63 | CacheCI_5_❌.webp | image/png | 256x202 | 161.0 | sha256:c42b137225ddc7c2…〔外〕 |
| 64 | CacheCI_60_👆.webp | image/png | 256x249 | 299.6 | sha256:88b64bc90dcdaad8…〔外〕 |
| 65 | CacheCI_61_🍺.webp | image/png | 227x256 | 105.8 | sha256:9b713326b9201775…〔外〕 |
| 66 | CacheCI_62_🔫.webp | image/png | 256x119 | 112.0 | sha256:8e746db20a507f06…〔外〕 |
| 67 | CacheCI_63_😇.webp | image/png | 256x256 | 132.2 | sha256:f17594c27a954c11…〔外〕 |
| 68 | CacheCI_64_🙊.webp | image/png | 256x192 | 247.3 | sha256:7ded42f19f26b769…〔外〕 |
| 69 | CacheCI_65_😭.webp | image/png | 204x256 | 173.9 | sha256:8e095d0b2ace86ec…〔外〕 |
| 70 | CacheCI_66_😾.webp | image/png | 256x256 | 95.3 | sha256:8759d17bc0cb8328…〔外〕 |
| 71 | CacheCI_67_😁.webp | image/png | 256x256 | 265.5 | sha256:42cfdba616df850d…〔外〕 |
| 72 | CacheCI_68_⚰.webp | image/png | 256x211 | 54.3 | sha256:77c24cc6d694a5af…〔外〕 |
| 73 | CacheCI_69_😁.webp | image/png | 256x188 | 220.2 | sha256:29012c4fa1458517…〔外〕 |
| 74 | CacheCI_6_🤔.webp | image/png | 256x256 | 105.9 | sha256:5732091a064179bd…〔外〕 |
| 75 | CacheCI_70_😮.webp | image/png | 236x256 | 230.9 | sha256:1ee89cb78c190f2f…〔外〕 |
| 76 | CacheCI_71_☠.webp | image/png | 256x62 | 32.0 | sha256:caa01ec3342ef43a…〔外〕 |
| 77 | CacheCI_72_🆕.webp | image/png | 256x192 | 402.1 | sha256:bac157a202244a73…〔外〕 |
| 78 | CacheCI_73_🐴.webp | image/png | 256x242 | 152.2 | sha256:d3ae1ae7de984404…〔外〕 |
| 79 | CacheCI_74_🛬.webp | image/png | 256x253 | 171.9 | sha256:94349c07e0059705…〔外〕 |
| 80 | CacheCI_75_🔫.webp | image/png | 256x75 | 44.3 | sha256:c9e117b2a1425e35…〔外〕 |
| 81 | CacheCI_76_🤣.webp | image/png | 256x238 | 180.1 | sha256:d44f509458a8e968…〔外〕 |
| 82 | CacheCI_77_😩.webp | image/png | 229x256 | 172.0 | sha256:92d0d56687b9412b…〔外〕 |
| 83 | CacheCI_78_👁.webp | image/png | 245x256 | 180.6 | sha256:04b017fa2c172c60…〔外〕 |
| 84 | CacheCI_79_🎞.webp | image/png | 256x189 | 211.7 | sha256:23b7faa479994224…〔外〕 |
| 85 | CacheCI_7_😭.webp | image/png | 214x256 | 112.9 | sha256:091518690fcdc030…〔外〕 |
| 86 | CacheCI_80_🤬.webp | image/png | 256x144 | 126.7 | sha256:a318eef5da3c8d48…〔外〕 |
| 87 | CacheCI_81_🎧.webp | image/png | 251x256 | 193.4 | sha256:6fb321f0beb97668…〔外〕 |
| 88 | CacheCI_82_😍.webp | image/png | 256x256 | 146.0 | sha256:bb6e71501c79efd3…〔外〕 |
| 89 | CacheCI_83_🥔.webp | image/png | 256x256 | 151.0 | sha256:beb175da5a07b001…〔外〕 |
| 90 | CacheCI_84_😅.webp | image/png | 256x256 | 218.2 | sha256:d4b2015f3fd5818e…〔外〕 |
| 91 | CacheCI_85_😄.webp | image/png | 256x244 | 229.9 | sha256:22561fc84113f7da…〔外〕 |
| 92 | CacheCI_86_🐋.webp | image/png | 256x144 | 110.6 | sha256:6661d0dec9c98aae…〔外〕 |
| 93 | CacheCI_87_🗣.webp | image/png | 238x256 | 210.4 | sha256:4d90b5e8314edaa0…〔外〕 |
| 94 | CacheCI_88_😎.webp | image/png | 256x256 | 217.9 | sha256:60f1193cf636a8c8…〔外〕 |
| 95 | CacheCI_89_🧃.webp | image/png | 256x256 | 230.1 | sha256:66908cce2957aa86…〔外〕 |
| 96 | CacheCI_8_👎.webp | image/png | 256x245 | 189.3 | sha256:d28bf3a06d488243…〔外〕 |
| 97 | CacheCI_90_🎛.webp | image/png | 256x256 | 704.6 | sha256:ca5077e6d421d48e…〔外〕 |
| 98 | CacheCI_91_👩‍💻.webp | image/png | 165x256 | 282.8 | sha256:586c134b159e9732…〔外〕 |
| 99 | CacheCI_92_😷.webp | image/png | 256x256 | 258.8 | sha256:47741b35ef24ba7e…〔外〕 |
| 100 | CacheCI_93_💩.webp | image/png | 153x256 | 160.1 | sha256:55cd7239fa6f3f51…〔外〕 |
| 101 | CacheCI_94_😇.webp | image/png | 256x256 | 275.0 | sha256:7244a6abcd9d04db…〔外〕 |
| 102 | CacheCI_95_⬜.webp | image/png | 256x256 | 2.1 | sha256:626f78df0ccb28d6…〔外〕 |
| 103 | CacheCI_96_🚖.webp | image/png | 193x256 | 342.6 | sha256:fcc343c4213da67d…〔外〕 |
| 104 | CacheCI_97_⛔.webp | image/png | 256x170 | 161.4 | sha256:050ea79721046c34…〔外〕 |
| 105 | CacheCI_98_😢.webp | image/png | 243x256 | 183.9 | sha256:b5c3b49f3b2ec89d…〔外〕 |
| 106 | CacheCI_99_💊.webp | image/png | 256x230 | 291.9 | sha256:89e606150744aaf3…〔外〕 |
| 107 | CacheCI_9_😃.webp | image/png | 256x256 | 162.9 | sha256:3db95dc5f05c6b72…〔外〕 |


## 6. `fuckgfwnewbie` — `fuckgfwnewbie.json`

- 標題:`fuckgfwnewbie`;包 ID:`fuckgfwnewbie`
- 張數:47;mimetype 分佈:image/png ×47
- 大小統計:合計 6,601,582 B(6.30 MB);平均 137.2 KB;最小 40.8 KB;最大 439.8 KB
- 來源 ID:sha256(外) ×47(全包皆為外部匯入條目)

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | fuckgfwnewbie_10_🤡.webp | image/png | 256x247 | 439.8 | sha256:664f9267bfc4d29c…〔外〕 |
| 2 | fuckgfwnewbie_11_🤺.webp | image/png | 256x256 | 159.7 | sha256:6a94d04ad4f60a86…〔外〕 |
| 3 | fuckgfwnewbie_12_🔍.webp | image/png | 255x256 | 61.4 | sha256:5bdb40a10e52e173…〔外〕 |
| 4 | fuckgfwnewbie_13_🚀.webp | image/png | 256x256 | 152.4 | sha256:fe8d3f5a706ca5fb…〔外〕 |
| 5 | fuckgfwnewbie_14_☝️.webp | image/png | 256x226 | 114.7 | sha256:4dbacc439a285ec2…〔外〕 |
| 6 | fuckgfwnewbie_15_🚇.webp | image/png | 256x256 | 210.2 | sha256:5dd8c02c349e5747…〔外〕 |
| 7 | fuckgfwnewbie_16_📮.webp | image/png | 256x256 | 182.4 | sha256:c5e896e2a12ffb1f…〔外〕 |
| 8 | fuckgfwnewbie_17_🚦.webp | image/png | 256x256 | 114.8 | sha256:2b031f8cee2cdffb…〔外〕 |
| 9 | fuckgfwnewbie_18_🚥.webp | image/png | 256x256 | 202.0 | sha256:8374ec810f118881…〔外〕 |
| 10 | fuckgfwnewbie_19_⬆️.webp | image/png | 256x217 | 121.4 | sha256:5b3b66c048660cc8…〔外〕 |
| 11 | fuckgfwnewbie_1_🤷‍♂️.webp | image/png | 256x256 | 139.7 | sha256:34c4c72804f3c65c…〔外〕 |
| 12 | fuckgfwnewbie_20_6️⃣.webp | image/png | 256x256 | 240.5 | sha256:a6740d631cb7ceea…〔外〕 |
| 13 | fuckgfwnewbie_21_🧩.webp | image/png | 256x256 | 203.6 | sha256:9ed722fb4cc5a7ff…〔外〕 |
| 14 | fuckgfwnewbie_22_🔀.webp | image/png | 256x200 | 114.2 | sha256:f75f10458534d700…〔外〕 |
| 15 | fuckgfwnewbie_23_📲.webp | image/png | 236x256 | 117.3 | sha256:cac406f4ff73c349…〔外〕 |
| 16 | fuckgfwnewbie_24_🗒.webp | image/png | 256x226 | 71.8 | sha256:01927e945f4c0ce9…〔外〕 |
| 17 | fuckgfwnewbie_25_ℹ️.webp | image/png | 256x171 | 128.2 | sha256:6d7d7dc276fb7be7…〔外〕 |
| 18 | fuckgfwnewbie_26_🧠.webp | image/png | 256x172 | 151.7 | sha256:922c3c41eec8270f…〔外〕 |
| 19 | fuckgfwnewbie_27_⛩.webp | image/png | 256x138 | 101.5 | sha256:14f9aa1242a5d00f…〔外〕 |
| 20 | fuckgfwnewbie_28_🔑.webp | image/png | 256x199 | 161.6 | sha256:09746f475d72e952…〔外〕 |
| 21 | fuckgfwnewbie_29_🗝.webp | image/png | 256x134 | 124.5 | sha256:e4ab48a77460f8fa…〔外〕 |
| 22 | fuckgfwnewbie_2_🚥.webp | image/png | 256x256 | 108.4 | sha256:c84874f6288ffe5d…〔外〕 |
| 23 | fuckgfwnewbie_30_👣.webp | image/png | 256x121 | 136.9 | sha256:238d426155a0d468…〔外〕 |
| 24 | fuckgfwnewbie_31_🐢.webp | image/png | 256x65 | 78.3 | sha256:ed22d03235e1274f…〔外〕 |
| 25 | fuckgfwnewbie_32_🍡.webp | image/png | 256x123 | 54.5 | sha256:df1cd5e58aad42d7…〔外〕 |
| 26 | fuckgfwnewbie_33_🍢.webp | image/png | 256x124 | 40.8 | sha256:58184eedaad9882b…〔外〕 |
| 27 | fuckgfwnewbie_34_🛳.webp | image/png | 256x234 | 63.2 | sha256:d1f3f59a577efc67…〔外〕 |
| 28 | fuckgfwnewbie_35_⛩.webp | image/png | 256x174 | 60.7 | sha256:5aa4aee1e8c04596…〔外〕 |
| 29 | fuckgfwnewbie_36_📖.webp | image/png | 256x256 | 106.4 | sha256:c51560090022e0c7…〔外〕 |
| 30 | fuckgfwnewbie_37_📄.webp | image/png | 256x256 | 53.7 | sha256:d59bc377e3107e69…〔外〕 |
| 31 | fuckgfwnewbie_38_💯.webp | image/png | 256x256 | 209.4 | sha256:6f0877c8d3b0ae7e…〔外〕 |
| 32 | fuckgfwnewbie_39_🈹.webp | image/png | 256x256 | 100.9 | sha256:b6668aee8da4a801…〔外〕 |
| 33 | fuckgfwnewbie_3_➿.webp | image/png | 222x256 | 207.6 | sha256:d669757449c9f9b7…〔外〕 |
| 34 | fuckgfwnewbie_40_🪟.webp | image/png | 256x256 | 89.6 | sha256:aa0cd7b6855c51f3…〔外〕 |
| 35 | fuckgfwnewbie_41_🖼.webp | image/png | 256x256 | 141.4 | sha256:4a00e11237106460…〔外〕 |
| 36 | fuckgfwnewbie_42_🎩.webp | image/png | 256x256 | 161.6 | sha256:f904dffb83233658…〔外〕 |
| 37 | fuckgfwnewbie_43_㊙️.webp | image/png | 256x105 | 67.2 | sha256:5c55daae075d445a…〔外〕 |
| 38 | fuckgfwnewbie_44_🤹‍♂️.webp | image/png | 256x165 | 117.9 | sha256:8cd0ecb6d3a87b93…〔外〕 |
| 39 | fuckgfwnewbie_45_📕.webp | image/png | 256x55 | 47.3 | sha256:7a5e1b4191a8ac3d…〔外〕 |
| 40 | fuckgfwnewbie_46_🤖.webp | image/png | 256x192 | 102.5 | sha256:4c2c5dc20ce427e4…〔外〕 |
| 41 | fuckgfwnewbie_47_😎.webp | image/png | 256x256 | 195.1 | sha256:c49dd0075224875c…〔外〕 |
| 42 | fuckgfwnewbie_4_➰.webp | image/png | 185x256 | 133.8 | sha256:f4574e20d136da01…〔外〕 |
| 43 | fuckgfwnewbie_5_❓.webp | image/png | 256x147 | 216.8 | sha256:da2aabb58142f52c…〔外〕 |
| 44 | fuckgfwnewbie_6_❔.webp | image/png | 256x167 | 235.3 | sha256:1c828289890ebcc7…〔外〕 |
| 45 | fuckgfwnewbie_7_😂.webp | image/png | 256x256 | 121.9 | sha256:165d8be20b11b42b…〔外〕 |
| 46 | fuckgfwnewbie_8_🤣.webp | image/png | 256x256 | 108.5 | sha256:15b24b04d29201d2…〔外〕 |
| 47 | fuckgfwnewbie_9_🎉.webp | image/png | 256x256 | 173.7 | sha256:91f1eb76308a799d…〔外〕 |


## 7. `suzumi_bili_2` — `suzumi_bili_2.json`

- 標題:`suzumi_bili_2`;包 ID:`suzumi_bili_2`
- 張數:111;mimetype 分佈:image/png ×111
- 大小統計:合計 23,240,093 B(22.16 MB);平均 204.5 KB;最小 13.5 KB;最大 306.0 KB
- 來源 ID:sha256(外) ×111(全包皆為外部匯入條目)

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | suzumi_bili_2_100_😥.webp | image/png | 256x256 | 208.1 | sha256:f447b0e19f59153e…〔外〕 |
| 2 | suzumi_bili_2_101_🤗.webp | image/png | 256x256 | 275.1 | sha256:c06956d5c4100849…〔外〕 |
| 3 | suzumi_bili_2_102_😎.webp | image/png | 256x256 | 214.0 | sha256:bf9acbde8b5ce49b…〔外〕 |
| 4 | suzumi_bili_2_103_🫠.webp | image/png | 256x256 | 159.3 | sha256:a8cc0fbc85f389d2…〔外〕 |
| 5 | suzumi_bili_2_104_🫥.webp | image/png | 256x256 | 205.6 | sha256:693c52597b21bcab…〔外〕 |
| 6 | suzumi_bili_2_105_😵‍💫.webp | image/png | 256x256 | 216.9 | sha256:29b8a6285dff00aa…〔外〕 |
| 7 | suzumi_bili_2_106_✊.webp | image/png | 256x256 | 191.1 | sha256:83bcb9cacf915e0d…〔外〕 |
| 8 | suzumi_bili_2_107_🥱.webp | image/png | 256x256 | 207.5 | sha256:5eb6223bbfc9c964…〔外〕 |
| 9 | suzumi_bili_2_108_🤕.webp | image/png | 256x256 | 257.4 | sha256:f95a81c1591f6ed1…〔外〕 |
| 10 | suzumi_bili_2_109_🍜.webp | image/png | 256x256 | 210.0 | sha256:14470c3bf93eb292…〔外〕 |
| 11 | suzumi_bili_2_10_😢.webp | image/png | 256x256 | 184.9 | sha256:08ecb68edb0dde76…〔外〕 |
| 12 | suzumi_bili_2_110_🙈.webp | image/png | 256x256 | 194.5 | sha256:be48236315f5f551…〔外〕 |
| 13 | suzumi_bili_2_111_💥.webp | image/png | 256x256 | 300.5 | sha256:fe32b64963b4b808…〔外〕 |
| 14 | suzumi_bili_2_11_😺.webp | image/png | 256x256 | 192.8 | sha256:805aa70eb1eb1312…〔外〕 |
| 15 | suzumi_bili_2_12_😖.webp | image/png | 256x256 | 149.9 | sha256:f0b9522780217805…〔外〕 |
| 16 | suzumi_bili_2_13_🤐.webp | image/png | 256x256 | 215.1 | sha256:c70b13b8a5475bb9…〔外〕 |
| 17 | suzumi_bili_2_14_😈.webp | image/png | 256x256 | 216.5 | sha256:4d0fc5317933912e…〔外〕 |
| 18 | suzumi_bili_2_15_😴.webp | image/png | 256x256 | 199.3 | sha256:1cb4a1bce057c9a5…〔外〕 |
| 19 | suzumi_bili_2_16_😵.webp | image/png | 256x256 | 156.6 | sha256:ee684dca2f07ccf4…〔外〕 |
| 20 | suzumi_bili_2_17_😭.webp | image/png | 256x256 | 183.5 | sha256:f254e8508e9f3f43…〔外〕 |
| 21 | suzumi_bili_2_18_🫨.webp | image/png | 256x256 | 182.4 | sha256:3a21a6c7c257f9f0…〔外〕 |
| 22 | suzumi_bili_2_19_🤛.webp | image/png | 256x256 | 185.7 | sha256:bc10cd1e1c9f88f6…〔外〕 |
| 23 | suzumi_bili_2_1_😵.webp | image/png | 256x256 | 186.1 | sha256:b364b7fd30d55220…〔外〕 |
| 24 | suzumi_bili_2_20_😸.webp | image/png | 256x256 | 198.6 | sha256:d1b486511c886d15…〔外〕 |
| 25 | suzumi_bili_2_21_😋.webp | image/png | 256x256 | 228.8 | sha256:491ab40c76d14f5b…〔外〕 |
| 26 | suzumi_bili_2_22_😐.webp | image/png | 256x256 | 174.5 | sha256:52aa24faf8a5c479…〔外〕 |
| 27 | suzumi_bili_2_23_😑.webp | image/png | 256x256 | 205.1 | sha256:ff31bce8ce354b15…〔外〕 |
| 28 | suzumi_bili_2_24_🤔.webp | image/png | 256x256 | 225.4 | sha256:e83b7bbf4aac89cf…〔外〕 |
| 29 | suzumi_bili_2_25_😢.webp | image/png | 256x256 | 195.0 | sha256:7001d2836671c258…〔外〕 |
| 30 | suzumi_bili_2_26_😤.webp | image/png | 256x256 | 176.5 | sha256:e19701638bd9b560…〔外〕 |
| 31 | suzumi_bili_2_27_😍.webp | image/png | 256x256 | 246.2 | sha256:e82a2bbfc780daf0…〔外〕 |
| 32 | suzumi_bili_2_28_☹️.webp | image/png | 256x256 | 206.5 | sha256:273bb93384fc7fa6…〔外〕 |
| 33 | suzumi_bili_2_29_🫶.webp | image/png | 256x256 | 245.6 | sha256:cbf478e75385cdc8…〔外〕 |
| 34 | suzumi_bili_2_2_😿.webp | image/png | 256x256 | 208.0 | sha256:f2d71d6191c3859b…〔外〕 |
| 35 | suzumi_bili_2_30_😱.webp | image/png | 256x256 | 187.9 | sha256:dff576a5d730e6a4…〔外〕 |
| 36 | suzumi_bili_2_31_🥰.webp | image/png | 256x256 | 222.7 | sha256:b748e7998e1dfc24…〔外〕 |
| 37 | suzumi_bili_2_32_😼.webp | image/png | 256x256 | 117.9 | sha256:adc58fef136c7716…〔外〕 |
| 38 | suzumi_bili_2_33_🍴.webp | image/png | 256x256 | 200.5 | sha256:d93de3d956ce35bd…〔外〕 |
| 39 | suzumi_bili_2_34_🥊.webp | image/png | 256x256 | 165.4 | sha256:2e24d8b55e737f64…〔外〕 |
| 40 | suzumi_bili_2_35_😘.webp | image/png | 256x256 | 229.4 | sha256:36c63d354a4fbb71…〔外〕 |
| 41 | suzumi_bili_2_36_😣.webp | image/png | 256x256 | 193.4 | sha256:0a14cd91fa9b775c…〔外〕 |
| 42 | suzumi_bili_2_37_😿.webp | image/png | 256x256 | 221.5 | sha256:54403ef1bc12df91…〔外〕 |
| 43 | suzumi_bili_2_38_❤️‍🩹.webp | image/png | 256x256 | 171.8 | sha256:8226bf08e966c883…〔外〕 |
| 44 | suzumi_bili_2_39_🪐.webp | image/png | 256x256 | 194.0 | sha256:2f973ccbbb13d9b3…〔外〕 |
| 45 | suzumi_bili_2_3_😻.webp | image/png | 256x256 | 193.0 | sha256:1c3fc0e126fb1718…〔外〕 |
| 46 | suzumi_bili_2_40_😶‍🌫️.webp | image/png | 256x256 | 106.0 | sha256:291a2b34f5bad469…〔外〕 |
| 47 | suzumi_bili_2_41_🫠.webp | image/png | 256x256 | 181.3 | sha256:8c5b4f0e172adfb1…〔外〕 |
| 48 | suzumi_bili_2_42_🥰.webp | image/png | 256x256 | 196.1 | sha256:c5581576daf63d60…〔外〕 |
| 49 | suzumi_bili_2_43_🫣.webp | image/png | 256x256 | 180.3 | sha256:0436f7fc60322d4b…〔外〕 |
| 50 | suzumi_bili_2_44_🤥.webp | image/png | 256x256 | 259.2 | sha256:42af86939fb8453e…〔外〕 |
| 51 | suzumi_bili_2_45_😵‍💫.webp | image/png | 256x256 | 243.9 | sha256:312a09d20d0916a8…〔外〕 |
| 52 | suzumi_bili_2_46_🦾.webp | image/png | 256x256 | 271.3 | sha256:c149186a7ea63ff0…〔外〕 |
| 53 | suzumi_bili_2_47_😋.webp | image/png | 256x256 | 224.7 | sha256:e685d834045111d9…〔外〕 |
| 54 | suzumi_bili_2_48_😐.webp | image/png | 256x256 | 278.3 | sha256:594d9644ec41cdcc…〔外〕 |
| 55 | suzumi_bili_2_49_😸.webp | image/png | 256x256 | 154.5 | sha256:aa31c675e6233eb4…〔外〕 |
| 56 | suzumi_bili_2_4_😺.webp | image/png | 256x256 | 187.6 | sha256:c67dde3bdb6edba2…〔外〕 |
| 57 | suzumi_bili_2_50_🔫.webp | image/png | 256x256 | 235.4 | sha256:fae72ec69fdd23ae…〔外〕 |
| 58 | suzumi_bili_2_51_💊.webp | image/png | 256x256 | 225.7 | sha256:873ce69637263a8f…〔外〕 |
| 59 | suzumi_bili_2_52_🔭.webp | image/png | 256x256 | 257.9 | sha256:26b9b1c4b15c2cf9…〔外〕 |
| 60 | suzumi_bili_2_53_👐.webp | image/png | 256x256 | 214.3 | sha256:e0e6679daba426a2…〔外〕 |
| 61 | suzumi_bili_2_54_✏️.webp | image/png | 256x256 | 170.2 | sha256:dab40ecdc69cf1ca…〔外〕 |
| 62 | suzumi_bili_2_55_🔮.webp | image/png | 256x256 | 306.0 | sha256:4c5d9d47da6e2efb…〔外〕 |
| 63 | suzumi_bili_2_56_🌁.webp | image/png | 256x256 | 169.0 | sha256:4e21e1b1eb853545…〔外〕 |
| 64 | suzumi_bili_2_57_🙃.webp | image/png | 256x256 | 123.9 | sha256:57665f4dd9cc2cb2…〔外〕 |
| 65 | suzumi_bili_2_58_😘.webp | image/png | 256x256 | 159.2 | sha256:50974d673912d46e…〔外〕 |
| 66 | suzumi_bili_2_59_🤗.webp | image/png | 256x256 | 230.9 | sha256:0a8cdf3637dfea7d…〔外〕 |
| 67 | suzumi_bili_2_5_👾.webp | image/png | 256x256 | 195.1 | sha256:62f7e741f6e3761c…〔外〕 |
| 68 | suzumi_bili_2_60_😺.webp | image/png | 256x256 | 151.3 | sha256:771b1536c7f17a72…〔外〕 |
| 69 | suzumi_bili_2_61_✈️.webp | image/png | 256x256 | 244.6 | sha256:25a23c8aa7f873ee…〔外〕 |
| 70 | suzumi_bili_2_62_😛.webp | image/png | 256x256 | 198.0 | sha256:32adf2e1fd52ac66…〔外〕 |
| 71 | suzumi_bili_2_63_✊.webp | image/png | 256x256 | 179.0 | sha256:0b5c72aecbce884c…〔外〕 |
| 72 | suzumi_bili_2_64_🤩.webp | image/png | 256x256 | 180.0 | sha256:fc5d465cdb4de74a…〔外〕 |
| 73 | suzumi_bili_2_65_🪀.webp | image/png | 256x256 | 232.2 | sha256:e8029ff4a84cd0d5…〔外〕 |
| 74 | suzumi_bili_2_66_😭.webp | image/png | 256x256 | 177.9 | sha256:d962d6d416414a65…〔外〕 |
| 75 | suzumi_bili_2_67_😶.webp | image/png | 256x256 | 13.5 | sha256:54d57175e8b94aed…〔外〕 |
| 76 | suzumi_bili_2_68_🫱.webp | image/png | 256x256 | 195.9 | sha256:0b27359bf9e94639…〔外〕 |
| 77 | suzumi_bili_2_69_🤚.webp | image/png | 256x256 | 114.8 | sha256:495329019f524468…〔外〕 |
| 78 | suzumi_bili_2_6_😃.webp | image/png | 256x256 | 212.3 | sha256:67a050c9cbd5fa06…〔外〕 |
| 79 | suzumi_bili_2_70_💔.webp | image/png | 256x256 | 302.0 | sha256:b31db4c2af10ec11…〔外〕 |
| 80 | suzumi_bili_2_71_🐱.webp | image/png | 256x256 | 221.6 | sha256:3c93a3d33a5e6f69…〔外〕 |
| 81 | suzumi_bili_2_72_😙.webp | image/png | 256x256 | 238.8 | sha256:88c676bf585d18d8…〔外〕 |
| 82 | suzumi_bili_2_73_🤗.webp | image/png | 256x256 | 270.5 | sha256:380ef12ad65ecaaa…〔外〕 |
| 83 | suzumi_bili_2_74_😇.webp | image/png | 256x256 | 198.8 | sha256:c685b3102fbde889…〔外〕 |
| 84 | suzumi_bili_2_75_🎂.webp | image/png | 256x256 | 285.8 | sha256:441dc8bd9ba88573…〔外〕 |
| 85 | suzumi_bili_2_76_😌.webp | image/png | 256x256 | 175.8 | sha256:b4c7f7900843cb90…〔外〕 |
| 86 | suzumi_bili_2_77_👍.webp | image/png | 256x256 | 184.3 | sha256:b9c0f1c9926c6394…〔外〕 |
| 87 | suzumi_bili_2_78_😽.webp | image/png | 256x256 | 189.0 | sha256:a09af8b2e40e3d70…〔外〕 |
| 88 | suzumi_bili_2_79_😉.webp | image/png | 256x256 | 226.5 | sha256:df49c3480d04fcab…〔外〕 |
| 89 | suzumi_bili_2_7_😫.webp | image/png | 256x256 | 181.8 | sha256:ec987a106f4daf7f…〔外〕 |
| 90 | suzumi_bili_2_80_😨.webp | image/png | 256x256 | 217.7 | sha256:6a5b36e24d694c44…〔外〕 |
| 91 | suzumi_bili_2_81_🫥.webp | image/png | 256x256 | 213.0 | sha256:2ccc625e8a0a06df…〔外〕 |
| 92 | suzumi_bili_2_82_😸.webp | image/png | 256x256 | 213.9 | sha256:93e1b07a4344ed5a…〔外〕 |
| 93 | suzumi_bili_2_83_🫣.webp | image/png | 256x256 | 223.9 | sha256:31ea05012d298092…〔外〕 |
| 94 | suzumi_bili_2_84_😑.webp | image/png | 256x256 | 194.3 | sha256:eadb367c66a02893…〔外〕 |
| 95 | suzumi_bili_2_85_😡.webp | image/png | 256x256 | 230.9 | sha256:42a6bbbb4e431086…〔外〕 |
| 96 | suzumi_bili_2_86_😵.webp | image/png | 256x256 | 91.1 | sha256:e36e5a00afa10176…〔外〕 |
| 97 | suzumi_bili_2_87_🤗.webp | image/png | 256x256 | 218.0 | sha256:e99f0aa062ca919d…〔外〕 |
| 98 | suzumi_bili_2_88_🥴.webp | image/png | 256x256 | 246.5 | sha256:eebd6c56e94676b0…〔外〕 |
| 99 | suzumi_bili_2_89_😭.webp | image/png | 256x256 | 217.5 | sha256:e2bce27d5c46caa4…〔外〕 |
| 100 | suzumi_bili_2_8_😌.webp | image/png | 256x256 | 194.1 | sha256:10a64c498ca423b4…〔外〕 |
| 101 | suzumi_bili_2_90_🤨.webp | image/png | 256x256 | 184.7 | sha256:c7560b39a798efe8…〔外〕 |
| 102 | suzumi_bili_2_91_🥳.webp | image/png | 256x256 | 205.7 | sha256:b31b8f40c9c18ef7…〔外〕 |
| 103 | suzumi_bili_2_92_🙃.webp | image/png | 256x256 | 204.5 | sha256:c4c98b99e4977b77…〔外〕 |
| 104 | suzumi_bili_2_93_🫠.webp | image/png | 256x256 | 285.2 | sha256:c1abcd21fea9ec38…〔外〕 |
| 105 | suzumi_bili_2_94_😿.webp | image/png | 256x256 | 186.5 | sha256:841af5b45231c4b8…〔外〕 |
| 106 | suzumi_bili_2_95_😿.webp | image/png | 256x256 | 208.9 | sha256:e265285be6d8cc7d…〔外〕 |
| 107 | suzumi_bili_2_96_😫.webp | image/png | 256x256 | 238.8 | sha256:180191a1afdb165b…〔外〕 |
| 108 | suzumi_bili_2_97_😶.webp | image/png | 256x256 | 234.5 | sha256:6444c2152f118ef4…〔外〕 |
| 109 | suzumi_bili_2_98_😋.webp | image/png | 256x256 | 216.2 | sha256:681d1f86cd4e4e06…〔外〕 |
| 110 | suzumi_bili_2_99_😋.webp | image/png | 256x256 | 216.1 | sha256:bd4ca1afc35964df…〔外〕 |
| 111 | suzumi_bili_2_9_😘.webp | image/png | 256x256 | 207.9 | sha256:847fdb68f28f8749…〔外〕 |


## 8. `NekoTempest` — `NekoTempest.json`

- 標題:`NekoTempest`;包 ID:`NekoTempest`
- 張數:73;mimetype 分佈:image/png ×73
- 大小統計:合計 15,378,859 B(14.67 MB);平均 205.7 KB;最小 49.1 KB;最大 468.8 KB
- 來源 ID:sha256(外) ×73(全包皆為外部匯入條目)

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | NekoTempest_10_😒.webp | image/png | 256x138 | 58.9 | sha256:94a862c055596f9a…〔外〕 |
| 2 | NekoTempest_11_🙃.webp | image/png | 256x255 | 160.1 | sha256:82c131d27b0c8097…〔外〕 |
| 3 | NekoTempest_12_😅.webp | image/png | 256x181 | 173.6 | sha256:f23f37b11b1258f1…〔外〕 |
| 4 | NekoTempest_13_🤔.webp | image/png | 256x256 | 296.6 | sha256:1ba42eb5df027b00…〔外〕 |
| 5 | NekoTempest_14_🥱.webp | image/png | 256x256 | 286.4 | sha256:883760e955dd68a8…〔外〕 |
| 6 | NekoTempest_15_😬.webp | image/png | 256x256 | 227.0 | sha256:7c286d8a7588b320…〔外〕 |
| 7 | NekoTempest_16_😣.webp | image/png | 256x256 | 314.5 | sha256:abeb5fd48b99726c…〔外〕 |
| 8 | NekoTempest_17_😌.webp | image/png | 256x256 | 312.7 | sha256:48b843996501beb4…〔外〕 |
| 9 | NekoTempest_18_😕.webp | image/png | 256x256 | 217.3 | sha256:f16389a0783e6984…〔外〕 |
| 10 | NekoTempest_19_😶.webp | image/png | 256x237 | 256.8 | sha256:544f0cf651a78e25…〔外〕 |
| 11 | NekoTempest_1_😤.webp | image/png | 256x170 | 239.2 | sha256:d25b69e89ad58d27…〔外〕 |
| 12 | NekoTempest_20_😦.webp | image/png | 256x256 | 242.3 | sha256:7bdc111acb20093f…〔外〕 |
| 13 | NekoTempest_21_😣.webp | image/png | 256x243 | 144.7 | sha256:41c2fa9ddef8fe81…〔外〕 |
| 14 | NekoTempest_22_👋.webp | image/png | 256x256 | 301.5 | sha256:aee12f80efdadc41…〔外〕 |
| 15 | NekoTempest_23_🤛.webp | image/png | 256x251 | 125.3 | sha256:03c8bb1a6d4b4dbb…〔外〕 |
| 16 | NekoTempest_24_😑.webp | image/png | 256x168 | 124.0 | sha256:0feb84cd5e03aa8f…〔外〕 |
| 17 | NekoTempest_25_🥵.webp | image/png | 256x170 | 253.7 | sha256:a0776b38fdda7486…〔外〕 |
| 18 | NekoTempest_26_😢.webp | image/png | 232x256 | 256.7 | sha256:7b83a08adf5f95cf…〔外〕 |
| 19 | NekoTempest_27_😣.webp | image/png | 256x187 | 177.6 | sha256:c91b73e758dab891…〔外〕 |
| 20 | NekoTempest_28_🥱.webp | image/png | 256x170 | 253.8 | sha256:5524d4f6f28d5948…〔外〕 |
| 21 | NekoTempest_29_😦.webp | image/png | 256x240 | 316.1 | sha256:a12e0cf684be8da3…〔外〕 |
| 22 | NekoTempest_2_😠.webp | image/png | 256x256 | 129.7 | sha256:2c059475867b283d…〔外〕 |
| 23 | NekoTempest_30_🤤.webp | image/png | 240x256 | 255.2 | sha256:5dd0b2b384a2b3f2…〔外〕 |
| 24 | NekoTempest_31_😴.webp | image/png | 256x256 | 277.8 | sha256:852cd8600634dee9…〔外〕 |
| 25 | NekoTempest_32_🤛.webp | image/png | 192x256 | 71.8 | sha256:bace7c9fbaaf4424…〔外〕 |
| 26 | NekoTempest_33_🤗.webp | image/png | 256x256 | 381.6 | sha256:d4848e1dab368b21…〔外〕 |
| 27 | NekoTempest_34_😦.webp | image/png | 256x168 | 75.2 | sha256:2ba7318140f2c889…〔外〕 |
| 28 | NekoTempest_35_😐.webp | image/png | 256x181 | 208.9 | sha256:8b4751065fd3bc6f…〔外〕 |
| 29 | NekoTempest_36_😿.webp | image/png | 256x253 | 288.4 | sha256:4a22eaf19b3a1f73…〔外〕 |
| 30 | NekoTempest_37_😔.webp | image/png | 256x193 | 180.1 | sha256:6b47ae29f23d2476…〔外〕 |
| 31 | NekoTempest_38_😖.webp | image/png | 256x253 | 252.0 | sha256:fbd4fb2f59234edc…〔外〕 |
| 32 | NekoTempest_39_😭.webp | image/png | 256x135 | 239.4 | sha256:72b025bf380ddc05…〔外〕 |
| 33 | NekoTempest_3_😒.webp | image/png | 256x242 | 223.7 | sha256:45632cc0d32cefcb…〔外〕 |
| 34 | NekoTempest_40_😴.webp | image/png | 256x215 | 139.1 | sha256:7cd353013a8f0e73…〔外〕 |
| 35 | NekoTempest_41_🥴.webp | image/png | 256x256 | 220.6 | sha256:939a0841754996eb…〔外〕 |
| 36 | NekoTempest_42_😐.webp | image/png | 256x137 | 75.6 | sha256:743b6bd81ab5d884…〔外〕 |
| 37 | NekoTempest_43_🤔.webp | image/png | 256x256 | 101.7 | sha256:7eba8c56053d5ec6…〔外〕 |
| 38 | NekoTempest_44_😄.webp | image/png | 188x256 | 268.4 | sha256:0c58c4208e9d020a…〔外〕 |
| 39 | NekoTempest_45_🙁.webp | image/png | 256x218 | 135.9 | sha256:3b999215d26a56d9…〔外〕 |
| 40 | NekoTempest_46_🙁.webp | image/png | 256x191 | 113.0 | sha256:4a16cfcbc06fb4ca…〔外〕 |
| 41 | NekoTempest_47_😯.webp | image/png | 242x256 | 241.2 | sha256:6c32cdb5fc4de569…〔外〕 |
| 42 | NekoTempest_48_😲.webp | image/png | 256x239 | 297.0 | sha256:4b574b4b7815f5a6…〔外〕 |
| 43 | NekoTempest_49_😥.webp | image/png | 256x256 | 248.2 | sha256:eebc7b66c0ccd34a…〔外〕 |
| 44 | NekoTempest_4_🤔.webp | image/png | 256x153 | 88.6 | sha256:6c2b3cfdb4793012…〔外〕 |
| 45 | NekoTempest_50_😶.webp | image/png | 256x160 | 143.1 | sha256:f841fb0c02db6a30…〔外〕 |
| 46 | NekoTempest_51_😶.webp | image/png | 256x151 | 54.2 | sha256:f3ad200d6933f03b…〔外〕 |
| 47 | NekoTempest_52_😠.webp | image/png | 256x221 | 161.2 | sha256:5efe44e6f7fdf08f…〔外〕 |
| 48 | NekoTempest_53_😡.webp | image/png | 256x254 | 116.6 | sha256:c9ed11540cf573e1…〔外〕 |
| 49 | NekoTempest_54_😑.webp | image/png | 256x256 | 184.6 | sha256:8d9db82e82b3d3fa…〔外〕 |
| 50 | NekoTempest_55_😒.webp | image/png | 178x256 | 90.6 | sha256:9f5bdccd089892d3…〔外〕 |
| 51 | NekoTempest_56_😞.webp | image/png | 256x208 | 130.4 | sha256:c828a9d42d805d1a…〔外〕 |
| 52 | NekoTempest_57_😯.webp | image/png | 256x168 | 86.6 | sha256:1d578f257a56a558…〔外〕 |
| 53 | NekoTempest_58_😶.webp | image/png | 256x256 | 215.4 | sha256:dc0aa2e99f810770…〔外〕 |
| 54 | NekoTempest_59_😐.webp | image/png | 256x192 | 128.3 | sha256:2cd26c95f64584c5…〔外〕 |
| 55 | NekoTempest_5_😶.webp | image/png | 256x251 | 159.2 | sha256:3870755b9a803eb1…〔外〕 |
| 56 | NekoTempest_60_😫.webp | image/png | 256x231 | 114.1 | sha256:0f2c476de8412bad…〔外〕 |
| 57 | NekoTempest_61_😴.webp | image/png | 256x170 | 155.8 | sha256:1f1ba4dcf3b41db4…〔外〕 |
| 58 | NekoTempest_62_😎.webp | image/png | 256x256 | 242.3 | sha256:9f995c74c222da62…〔外〕 |
| 59 | NekoTempest_63_😴.webp | image/png | 256x191 | 275.1 | sha256:3aee1000faffd716…〔外〕 |
| 60 | NekoTempest_64_😥.webp | image/png | 256x190 | 193.3 | sha256:be0d06c0b1af444d…〔外〕 |
| 61 | NekoTempest_65_🥰.webp | image/png | 256x256 | 468.8 | sha256:47dc65ce5ae5d334…〔外〕 |
| 62 | NekoTempest_66_😦.webp | image/png | 256x256 | 387.1 | sha256:0a0bd43072a34085…〔外〕 |
| 63 | NekoTempest_67_😇.webp | image/png | 256x256 | 286.8 | sha256:afe2bf54a08ad87f…〔外〕 |
| 64 | NekoTempest_68_😒.webp | image/png | 256x256 | 360.4 | sha256:d9e06c36783f57c9…〔外〕 |
| 65 | NekoTempest_69_😠.webp | image/png | 256x256 | 189.7 | sha256:988ff15fde40d5e7…〔外〕 |
| 66 | NekoTempest_6_😐.webp | image/png | 256x256 | 49.1 | sha256:96d1e92e9ac54d5d…〔外〕 |
| 67 | NekoTempest_70_😢.webp | image/png | 256x256 | 310.3 | sha256:26afcf026eae8835…〔外〕 |
| 68 | NekoTempest_71_😐.webp | image/png | 256x219 | 165.7 | sha256:49cd7ae77682e4e3…〔外〕 |
| 69 | NekoTempest_72_😅.webp | image/png | 210x256 | 186.4 | sha256:e81a26d07a667d2a…〔外〕 |
| 70 | NekoTempest_73_😅.webp | image/png | 220x256 | 290.1 | sha256:8e72726f96fda98e…〔外〕 |
| 71 | NekoTempest_7_🤨.webp | image/png | 256x182 | 128.2 | sha256:623668607046efdc…〔外〕 |
| 72 | NekoTempest_8_🤨.webp | image/png | 216x256 | 224.4 | sha256:fcb36dfc943fc958…〔外〕 |
| 73 | NekoTempest_9_😅.webp | image/png | 256x243 | 268.4 | sha256:736dd49bbd21f068…〔外〕 |


## 9. `Qing_by_NaiDrawBot` — `Qing_by_NaiDrawBot.json`

- 標題:`Qing_by_NaiDrawBot`;包 ID:`Qing_by_NaiDrawBot`
- 張數:23;mimetype 分佈:image/png ×23
- 大小統計:合計 4,649,518 B(4.43 MB);平均 197.4 KB;最小 116.6 KB;最大 270.3 KB
- 來源 ID:sha256(外) ×23(全包皆為外部匯入條目)

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | Qing_by_NaiDrawBot_10_🤬.webm | image/png | 256x256 | 220.8 | sha256:306ed838665581a3…〔外〕 |
| 2 | Qing_by_NaiDrawBot_11_❤️.webm | image/png | 256x256 | 227.8 | sha256:3f52200a67f2ea1f…〔外〕 |
| 3 | Qing_by_NaiDrawBot_12_👩.webm | image/png | 256x256 | 191.4 | sha256:a3e60893625ad600…〔外〕 |
| 4 | Qing_by_NaiDrawBot_13_🛩️.webm | image/png | 256x256 | 163.2 | sha256:dddabc67d4d239a1…〔外〕 |
| 5 | Qing_by_NaiDrawBot_14_💀.webm | image/png | 256x256 | 194.2 | sha256:db25d7dd95ff53bb…〔外〕 |
| 6 | Qing_by_NaiDrawBot_15_🔓.webm | image/png | 256x256 | 173.1 | sha256:7d9d8fc0c5c3fbbb…〔外〕 |
| 7 | Qing_by_NaiDrawBot_16_👶.webm | image/png | 256x256 | 160.6 | sha256:ca78979a4575ba5f…〔外〕 |
| 8 | Qing_by_NaiDrawBot_17_🚫.webm | image/png | 256x256 | 242.9 | sha256:bd6571035738105f…〔外〕 |
| 9 | Qing_by_NaiDrawBot_18_😮.webm | image/png | 256x256 | 203.5 | sha256:01d9c65a5fb85662…〔外〕 |
| 10 | Qing_by_NaiDrawBot_19_👍.webm | image/png | 256x256 | 270.3 | sha256:f01f8e9ca3549d9a…〔外〕 |
| 11 | Qing_by_NaiDrawBot_1_👤.webm | image/png | 256x256 | 184.9 | sha256:1839116a24163a2e…〔外〕 |
| 12 | Qing_by_NaiDrawBot_20_🔓.webm | image/png | 256x256 | 157.6 | sha256:aa67f56222fc6563…〔外〕 |
| 13 | Qing_by_NaiDrawBot_21_🥊.webm | image/png | 256x256 | 203.7 | sha256:9734820569572ece…〔外〕 |
| 14 | Qing_by_NaiDrawBot_22_👤.webm | image/png | 256x256 | 204.8 | sha256:13b0271dde08ed31…〔外〕 |
| 15 | Qing_by_NaiDrawBot_23_📦.webm | image/png | 256x256 | 238.2 | sha256:a4c0588c04c40981…〔外〕 |
| 16 | Qing_by_NaiDrawBot_2_😭.webm | image/png | 256x256 | 192.0 | sha256:d625d8d0b34c66c8…〔外〕 |
| 17 | Qing_by_NaiDrawBot_3_🌟.webm | image/png | 256x256 | 200.6 | sha256:4889ef2809b52788…〔外〕 |
| 18 | Qing_by_NaiDrawBot_4_🌿.webm | image/png | 256x256 | 222.6 | sha256:023a2d610ecb0314…〔外〕 |
| 19 | Qing_by_NaiDrawBot_5_🐱.webm | image/png | 256x256 | 183.7 | sha256:8be50aa830dd337e…〔外〕 |
| 20 | Qing_by_NaiDrawBot_6_😴.webm | image/png | 256x256 | 165.3 | sha256:cdaee0d646819d86…〔外〕 |
| 21 | Qing_by_NaiDrawBot_7_😏.webm | image/png | 256x256 | 216.4 | sha256:cffe382ed1550415…〔外〕 |
| 22 | Qing_by_NaiDrawBot_8_❤️.webm | image/png | 256x256 | 116.6 | sha256:0fb2262959bfd940…〔外〕 |
| 23 | Qing_by_NaiDrawBot_9_😄.webm | image/png | 256x256 | 206.5 | sha256:b9a7b211be0504d0…〔外〕 |


## 10. `Togawa_Sakiko_1b` — `Togawa_Sakiko_1b.json`

- 標題:`Togawa_Sakiko_1b`;包 ID:`Togawa_Sakiko_1b`
- 張數:20;mimetype 分佈:image/png ×20
- 大小統計:合計 4,853,865 B(4.63 MB);平均 237.0 KB;最小 167.1 KB;最大 302.8 KB
- 來源 ID:sha256(外) ×20(全包皆為外部匯入條目)

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | Togawa_Sakiko_1b_10_😭.webm | image/png | 256x256 | 240.9 | sha256:1dae427d54cf0edf…〔外〕 |
| 2 | Togawa_Sakiko_1b_11_😇.webm | image/png | 256x256 | 198.3 | sha256:f5c9781cdbf4c3d4…〔外〕 |
| 3 | Togawa_Sakiko_1b_12_📱.webm | image/png | 256x256 | 212.0 | sha256:0d768bd84e430cc0…〔外〕 |
| 4 | Togawa_Sakiko_1b_13_👀.webm | image/png | 256x256 | 167.1 | sha256:03821c112e5f5e32…〔外〕 |
| 5 | Togawa_Sakiko_1b_14_🥰.webm | image/png | 256x256 | 233.9 | sha256:9695b9ef754c7612…〔外〕 |
| 6 | Togawa_Sakiko_1b_15_🥹.webm | image/png | 256x256 | 170.7 | sha256:58abc7d6c146f358…〔外〕 |
| 7 | Togawa_Sakiko_1b_16_😠.webm | image/png | 256x256 | 253.6 | sha256:1deb22e1e2affd1e…〔外〕 |
| 8 | Togawa_Sakiko_1b_17_❌.webm | image/png | 256x256 | 243.7 | sha256:4465f7a56079e49b…〔外〕 |
| 9 | Togawa_Sakiko_1b_18_😅.webm | image/png | 256x256 | 236.4 | sha256:826f0a3cdce6c689…〔外〕 |
| 10 | Togawa_Sakiko_1b_19_😋.webm | image/png | 256x256 | 249.1 | sha256:38bc153699c9e27d…〔外〕 |
| 11 | Togawa_Sakiko_1b_1_🤗.webm | image/png | 256x256 | 262.1 | sha256:732e26b70f1bd86b…〔外〕 |
| 12 | Togawa_Sakiko_1b_20_🤣.webm | image/png | 256x256 | 251.2 | sha256:4b1bca29d21129de…〔外〕 |
| 13 | Togawa_Sakiko_1b_2_😈.webm | image/png | 256x256 | 220.3 | sha256:4846e18161313d2f…〔外〕 |
| 14 | Togawa_Sakiko_1b_3_😋.webm | image/png | 256x256 | 247.4 | sha256:20e511038fd83d49…〔外〕 |
| 15 | Togawa_Sakiko_1b_4_😅.webm | image/png | 256x256 | 261.4 | sha256:0d6c2439cc0aa5fa…〔外〕 |
| 16 | Togawa_Sakiko_1b_5_🫢.webm | image/png | 256x256 | 242.0 | sha256:1fc06b0a90f80bd4…〔外〕 |
| 17 | Togawa_Sakiko_1b_6_🖕.webm | image/png | 256x256 | 243.4 | sha256:476f14ece36556fb…〔外〕 |
| 18 | Togawa_Sakiko_1b_7_👌.webm | image/png | 256x256 | 234.9 | sha256:8ba94d8edfd42589…〔外〕 |
| 19 | Togawa_Sakiko_1b_8_🧋.webm | image/png | 256x256 | 268.8 | sha256:6c4b7e43b82f85a8…〔外〕 |
| 20 | Togawa_Sakiko_1b_9_🤔.webm | image/png | 256x256 | 302.8 | sha256:2c154a0645b3a228…〔外〕 |


## 11. `X264WebmPack` — `X264WebmPack.json`

- 標題:`X264WebmPack`;包 ID:`X264WebmPack`
- 張數:34;mimetype 分佈:image/png ×34
- 大小統計:合計 10,644,538 B(10.15 MB);平均 305.7 KB;最小 181.8 KB;最大 496.2 KB
- 來源 ID:sha256(外) ×34(全包皆為外部匯入條目)

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | X264WebmPack_10_😄.webm | image/png | 256x256 | 226.4 | sha256:71956c557ceaf13a…〔外〕 |
| 2 | X264WebmPack_11_👋.webm | image/png | 256x256 | 306.2 | sha256:06cf5bdf21310a27…〔外〕 |
| 3 | X264WebmPack_12_😡.webm | image/png | 256x192 | 193.2 | sha256:a3b64565accfa349…〔外〕 |
| 4 | X264WebmPack_13_🔨.webm | image/png | 256x256 | 192.2 | sha256:2d4b70da71c3bbd6…〔外〕 |
| 5 | X264WebmPack_14_❔.webm | image/png | 256x256 | 234.8 | sha256:5262f030fa060229…〔外〕 |
| 6 | X264WebmPack_15_🚫.webm | image/png | 256x256 | 466.4 | sha256:2757273e8a875ba5…〔外〕 |
| 7 | X264WebmPack_16_😶.webm | image/png | 256x256 | 367.4 | sha256:c28283dfccae0274…〔外〕 |
| 8 | X264WebmPack_17_😡.webm | image/png | 256x256 | 329.1 | sha256:c1a926d9717440ab…〔外〕 |
| 9 | X264WebmPack_18_😶.webm | image/png | 256x256 | 349.0 | sha256:df4451f4da521daa…〔外〕 |
| 10 | X264WebmPack_19_🙇.webm | image/png | 256x252 | 277.5 | sha256:524097a8fea36504…〔外〕 |
| 11 | X264WebmPack_1_😈.webm | image/png | 256x256 | 391.1 | sha256:772872229a0abd32…〔外〕 |
| 12 | X264WebmPack_20_😕.webm | image/png | 256x256 | 256.5 | sha256:6589cc00c5a3a273…〔外〕 |
| 13 | X264WebmPack_21_😅.webm | image/png | 256x256 | 341.0 | sha256:f32e0c3c3513e597…〔外〕 |
| 14 | X264WebmPack_22_👀.webm | image/png | 256x256 | 253.1 | sha256:4032d24be109f07f…〔外〕 |
| 15 | X264WebmPack_23_👅.webm | image/png | 256x256 | 328.7 | sha256:5fc9b6a86757460f…〔外〕 |
| 16 | X264WebmPack_24_😭.webm | image/png | 256x256 | 352.0 | sha256:2c32850eb3f0191c…〔外〕 |
| 17 | X264WebmPack_25_😒.webm | image/png | 256x256 | 249.4 | sha256:0fdfe112ce7f8c83…〔外〕 |
| 18 | X264WebmPack_26_😯.webm | image/png | 256x256 | 385.2 | sha256:bcf89b6196513316…〔外〕 |
| 19 | X264WebmPack_27_😭.webm | image/png | 256x256 | 283.6 | sha256:e8443f3525f5407e…〔外〕 |
| 20 | X264WebmPack_28_😺.webm | image/png | 256x256 | 395.9 | sha256:ab250d5f02ae2b48…〔外〕 |
| 21 | X264WebmPack_29_😞.webm | image/png | 256x256 | 433.2 | sha256:ecda240cb6eabede…〔外〕 |
| 22 | X264WebmPack_2_🍊.webm | image/png | 256x256 | 312.6 | sha256:4ddd8d7888d23d8f…〔外〕 |
| 23 | X264WebmPack_30_😈.webm | image/png | 256x256 | 259.8 | sha256:1b39e19c88646ec3…〔外〕 |
| 24 | X264WebmPack_31_🌸.webm | image/png | 256x256 | 191.2 | sha256:3e2c8254643803ab…〔外〕 |
| 25 | X264WebmPack_32_💰.webm | image/png | 256x256 | 496.2 | sha256:bd205a0c37ceff35…〔外〕 |
| 26 | X264WebmPack_33_🐈.webm | image/png | 256x256 | 305.1 | sha256:c7e70cfea64e0151…〔外〕 |
| 27 | X264WebmPack_34_🔨.webm | image/png | 256x256 | 321.8 | sha256:6eb8674fa4fb8614…〔外〕 |
| 28 | X264WebmPack_3_🐾.webm | image/png | 256x256 | 181.8 | sha256:989206c916b7ff9e…〔外〕 |
| 29 | X264WebmPack_4_🐱.webm | image/png | 256x256 | 288.4 | sha256:5644956d1766f7eb…〔外〕 |
| 30 | X264WebmPack_5_😤.webm | image/png | 256x256 | 296.5 | sha256:1b01587ae54646c5…〔外〕 |
| 31 | X264WebmPack_6_🌙.webm | image/png | 256x256 | 287.1 | sha256:3361b94d3fa447f8…〔外〕 |
| 32 | X264WebmPack_7_🔨.webm | image/png | 256x256 | 212.9 | sha256:818fc18761dbf227…〔外〕 |
| 33 | X264WebmPack_8_🌂.webm | image/png | 256x256 | 357.1 | sha256:1d2a100007c72a4c…〔外〕 |
| 34 | X264WebmPack_9_😅.webm | image/png | 256x256 | 272.7 | sha256:16fcd9475b4fd4dc…〔外〕 |


## 12. `b675aff8_by_fStikBot` — `b675aff8_by_fStikBot.json`

- 標題:`b675aff8_by_fStikBot`;包 ID:`b675aff8_by_fStikBot`
- 張數:101;mimetype 分佈:image/png ×101
- 大小統計:合計 18,694,330 B(17.83 MB);平均 180.8 KB;最小 43.5 KB;最大 444.7 KB
- 來源 ID:sha256(外) ×101(全包皆為外部匯入條目)

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | b675aff8_by_fStikBot_100_🍡.webp | image/png | 256x229 | 262.9 | sha256:c57774250da98fee…〔外〕 |
| 2 | b675aff8_by_fStikBot_101_🌟.webp | image/png | 256x236 | 217.8 | sha256:8e5f0a6bdbbbfbf4…〔外〕 |
| 3 | b675aff8_by_fStikBot_10_🌿.webp | image/png | 256x256 | 63.2 | sha256:5c7462e26a315818…〔外〕 |
| 4 | b675aff8_by_fStikBot_11_💊.webp | image/png | 256x256 | 444.7 | sha256:fff684c0a6692e8f…〔外〕 |
| 5 | b675aff8_by_fStikBot_12_😅.webp | image/png | 256x256 | 218.2 | sha256:794e9e161572ae01…〔外〕 |
| 6 | b675aff8_by_fStikBot_13_😃.webp | image/png | 233x256 | 299.7 | sha256:b130f9eacb27da98…〔外〕 |
| 7 | b675aff8_by_fStikBot_14_😃.webp | image/png | 256x119 | 144.5 | sha256:505343bea48397b2…〔外〕 |
| 8 | b675aff8_by_fStikBot_15_👀.webp | image/png | 256x204 | 111.5 | sha256:4f4f93f297f03960…〔外〕 |
| 9 | b675aff8_by_fStikBot_16_👀.webp | image/png | 256x219 | 262.8 | sha256:caf0ea7679b7b093…〔外〕 |
| 10 | b675aff8_by_fStikBot_17_😭.webp | image/png | 256x256 | 171.4 | sha256:2177ae37adb7e402…〔外〕 |
| 11 | b675aff8_by_fStikBot_18_0️⃣.webp | image/png | 256x100 | 43.5 | sha256:498fb7022ce7a12a…〔外〕 |
| 12 | b675aff8_by_fStikBot_19_💀.webp | image/png | 241x256 | 120.6 | sha256:f03baaa4b603fffa…〔外〕 |
| 13 | b675aff8_by_fStikBot_1_🥲.webp | image/png | 246x256 | 270.4 | sha256:8503d76f18d32fef…〔外〕 |
| 14 | b675aff8_by_fStikBot_20_😃.webp | image/png | 256x222 | 173.0 | sha256:4296f6980519e964…〔外〕 |
| 15 | b675aff8_by_fStikBot_21_🤔.webp | image/png | 242x256 | 165.7 | sha256:8e6732988798f0d4…〔外〕 |
| 16 | b675aff8_by_fStikBot_22_😫.webp | image/png | 256x134 | 72.2 | sha256:68613754b09a630b…〔外〕 |
| 17 | b675aff8_by_fStikBot_23_➕.webp | image/png | 256x256 | 292.2 | sha256:f27015f6a222cfc3…〔外〕 |
| 18 | b675aff8_by_fStikBot_24_😱.webp | image/png | 256x239 | 169.0 | sha256:71764a32f872f8f9…〔外〕 |
| 19 | b675aff8_by_fStikBot_25_🧐.webp | image/png | 256x256 | 74.3 | sha256:5b01c2299d03f0f4…〔外〕 |
| 20 | b675aff8_by_fStikBot_26_🧐.webp | image/png | 256x242 | 182.3 | sha256:5ffa2e451a163538…〔外〕 |
| 21 | b675aff8_by_fStikBot_27_🥱.webp | image/png | 256x256 | 93.0 | sha256:33d00907a9f12eec…〔外〕 |
| 22 | b675aff8_by_fStikBot_28_👍.webp | image/png | 256x256 | 65.9 | sha256:f294aaefd54fe86b…〔外〕 |
| 23 | b675aff8_by_fStikBot_29_🍵.webp | image/png | 256x256 | 165.0 | sha256:bc6dd795676a7442…〔外〕 |
| 24 | b675aff8_by_fStikBot_2_😃.webp | image/png | 256x192 | 175.4 | sha256:89b1d22c36621b50…〔外〕 |
| 25 | b675aff8_by_fStikBot_30_🍵.webp | image/png | 254x256 | 221.5 | sha256:c1e43a81868dd391…〔外〕 |
| 26 | b675aff8_by_fStikBot_31_😢.webp | image/png | 256x256 | 82.0 | sha256:ecca10dd4edb4f8a…〔外〕 |
| 27 | b675aff8_by_fStikBot_32_🐴.webp | image/png | 253x256 | 155.8 | sha256:67a597a3e02fdc25…〔外〕 |
| 28 | b675aff8_by_fStikBot_33_🤔.webp | image/png | 256x85 | 97.9 | sha256:8d56afc1a92751cf…〔外〕 |
| 29 | b675aff8_by_fStikBot_34_⚠️.webp | image/png | 256x197 | 78.7 | sha256:15a242e7e971ced2…〔外〕 |
| 30 | b675aff8_by_fStikBot_35_✨.webp | image/png | 256x256 | 154.2 | sha256:1de6db867acbe5e9…〔外〕 |
| 31 | b675aff8_by_fStikBot_36_✔️.webp | image/png | 256x256 | 120.5 | sha256:f6b5d9403dd4319c…〔外〕 |
| 32 | b675aff8_by_fStikBot_37_🛏.webp | image/png | 256x256 | 164.9 | sha256:3cebc62f0f24ab10…〔外〕 |
| 33 | b675aff8_by_fStikBot_38_❗.webp | image/png | 209x256 | 187.2 | sha256:e473f835cf907186…〔外〕 |
| 34 | b675aff8_by_fStikBot_39_🤔.webp | image/png | 200x256 | 179.5 | sha256:84e4eb423a357855…〔外〕 |
| 35 | b675aff8_by_fStikBot_3_😃.webp | image/png | 194x256 | 249.9 | sha256:159cad90619db286…〔外〕 |
| 36 | b675aff8_by_fStikBot_40_🚇.webp | image/png | 256x256 | 296.0 | sha256:ffbd30e89c4a06a4…〔外〕 |
| 37 | b675aff8_by_fStikBot_41_😃.webp | image/png | 256x221 | 143.1 | sha256:be926019b287035e…〔外〕 |
| 38 | b675aff8_by_fStikBot_42_😃.webp | image/png | 191x256 | 167.1 | sha256:e6e06243ff6deeba…〔外〕 |
| 39 | b675aff8_by_fStikBot_43_😮.webp | image/png | 256x256 | 104.2 | sha256:7eb29a5f3777547d…〔外〕 |
| 40 | b675aff8_by_fStikBot_44_😃.webp | image/png | 214x256 | 56.5 | sha256:511b224c45a4f69b…〔外〕 |
| 41 | b675aff8_by_fStikBot_45_✨.webp | image/png | 256x256 | 163.7 | sha256:7aa4b29da940a226…〔外〕 |
| 42 | b675aff8_by_fStikBot_46_📣.webp | image/png | 256x256 | 131.1 | sha256:48ae0da824dea878…〔外〕 |
| 43 | b675aff8_by_fStikBot_47_❓.webp | image/png | 256x256 | 178.2 | sha256:61be128cdff407f9…〔外〕 |
| 44 | b675aff8_by_fStikBot_48_🙏.webp | image/png | 256x225 | 193.2 | sha256:e4e6023516cdfb5e…〔外〕 |
| 45 | b675aff8_by_fStikBot_49_🍉.webp | image/png | 256x211 | 138.5 | sha256:194003467a5cd343…〔外〕 |
| 46 | b675aff8_by_fStikBot_4_😃.webp | image/png | 256x243 | 233.8 | sha256:58055ca4ce83e89a…〔外〕 |
| 47 | b675aff8_by_fStikBot_50_✨.webp | image/png | 256x145 | 111.9 | sha256:96f67225f0f60e97…〔外〕 |
| 48 | b675aff8_by_fStikBot_51_✨.webp | image/png | 256x251 | 399.0 | sha256:e28ecf5fe6b02f5b…〔外〕 |
| 49 | b675aff8_by_fStikBot_52_🥶.webp | image/png | 256x192 | 76.2 | sha256:55b094f4de1db6fe…〔外〕 |
| 50 | b675aff8_by_fStikBot_53_🌿.webp | image/png | 256x194 | 201.5 | sha256:604cb79068a81b5e…〔外〕 |
| 51 | b675aff8_by_fStikBot_54_🍵.webp | image/png | 256x228 | 129.4 | sha256:0c5bd2cc2477640d…〔外〕 |
| 52 | b675aff8_by_fStikBot_55_🧠.webp | image/png | 256x139 | 88.8 | sha256:5b634c8d10f5c448…〔外〕 |
| 53 | b675aff8_by_fStikBot_56_💴.webp | image/png | 256x158 | 203.7 | sha256:a4b89f5088b8b40b…〔外〕 |
| 54 | b675aff8_by_fStikBot_57_📲.webp | image/png | 256x256 | 245.3 | sha256:a686223002244d29…〔外〕 |
| 55 | b675aff8_by_fStikBot_58_💥.webp | image/png | 256x248 | 201.0 | sha256:91c65cbd82efccff…〔外〕 |
| 56 | b675aff8_by_fStikBot_59_💥.webp | image/png | 256x232 | 303.1 | sha256:7249d08bf057aae8…〔外〕 |
| 57 | b675aff8_by_fStikBot_5_😃.webp | image/png | 256x192 | 208.3 | sha256:9469da733c30ee6d…〔外〕 |
| 58 | b675aff8_by_fStikBot_60_✨.webp | image/png | 256x256 | 143.1 | sha256:0358f521decf2342…〔外〕 |
| 59 | b675aff8_by_fStikBot_61_✅.webp | image/png | 169x256 | 94.4 | sha256:cb36241193693804…〔外〕 |
| 60 | b675aff8_by_fStikBot_62_🔨.webp | image/png | 256x223 | 184.5 | sha256:e2ef375a59ce2c37…〔外〕 |
| 61 | b675aff8_by_fStikBot_63_🥵.webp | image/png | 256x250 | 174.3 | sha256:5accfcd60cb7630e…〔外〕 |
| 62 | b675aff8_by_fStikBot_64_❓.webp | image/png | 230x256 | 98.7 | sha256:a068497fa6d5ab44…〔外〕 |
| 63 | b675aff8_by_fStikBot_65_🔨.webp | image/png | 256x243 | 261.8 | sha256:574a8b925d79941d…〔外〕 |
| 64 | b675aff8_by_fStikBot_66_🛌.webp | image/png | 256x134 | 121.5 | sha256:724a45138f4321de…〔外〕 |
| 65 | b675aff8_by_fStikBot_67_✨.webp | image/png | 256x133 | 148.4 | sha256:139c432efcf79540…〔外〕 |
| 66 | b675aff8_by_fStikBot_68_✨.webp | image/png | 251x256 | 94.9 | sha256:15b0a44f6873df99…〔外〕 |
| 67 | b675aff8_by_fStikBot_69_😒.webp | image/png | 256x256 | 304.7 | sha256:1426f8940e641995…〔外〕 |
| 68 | b675aff8_by_fStikBot_6_😃.webp | image/png | 256x256 | 303.9 | sha256:f70f041fbce32e28…〔外〕 |
| 69 | b675aff8_by_fStikBot_70_💰.webp | image/png | 256x166 | 53.7 | sha256:1cab9d1a2d038042…〔外〕 |
| 70 | b675aff8_by_fStikBot_71_✨.webp | image/png | 256x255 | 140.1 | sha256:5fff4e10d83510d9…〔外〕 |
| 71 | b675aff8_by_fStikBot_72_🤬.webp | image/png | 235x256 | 305.7 | sha256:33c55c3fa8c09c09…〔外〕 |
| 72 | b675aff8_by_fStikBot_73_✨.webp | image/png | 256x244 | 229.7 | sha256:1a579d767ce552bc…〔外〕 |
| 73 | b675aff8_by_fStikBot_74_😁.webp | image/png | 256x256 | 104.7 | sha256:eb8fad509cce60a3…〔外〕 |
| 74 | b675aff8_by_fStikBot_75_✨.webp | image/png | 256x202 | 249.1 | sha256:8cc5363319867618…〔外〕 |
| 75 | b675aff8_by_fStikBot_76_✨.webp | image/png | 256x252 | 256.2 | sha256:ceb1e5ea5122e402…〔外〕 |
| 76 | b675aff8_by_fStikBot_77_✨.webp | image/png | 256x256 | 182.1 | sha256:8db0ea32dd791200…〔外〕 |
| 77 | b675aff8_by_fStikBot_78_✨.webp | image/png | 171x256 | 284.9 | sha256:819087c691f4608e…〔外〕 |
| 78 | b675aff8_by_fStikBot_79_😁.webp | image/png | 256x256 | 148.9 | sha256:48bb1a606b20f16a…〔外〕 |
| 79 | b675aff8_by_fStikBot_7_😃.webp | image/png | 246x256 | 180.4 | sha256:fd5eea5aa1aa310a…〔外〕 |
| 80 | b675aff8_by_fStikBot_80_😭.webp | image/png | 256x225 | 290.3 | sha256:5e6c48b0afed56ff…〔外〕 |
| 81 | b675aff8_by_fStikBot_81_🤤.webp | image/png | 256x190 | 90.3 | sha256:c336fc6dc3d06a0b…〔外〕 |
| 82 | b675aff8_by_fStikBot_82_👨‍🦳.webp | image/png | 256x256 | 420.8 | sha256:a77b4271f5220d4a…〔外〕 |
| 83 | b675aff8_by_fStikBot_83_⚡.webp | image/png | 256x205 | 193.8 | sha256:b87b014bf66d9dd6…〔外〕 |
| 84 | b675aff8_by_fStikBot_84_📹.webp | image/png | 256x205 | 185.7 | sha256:73d2a1ae75fcfad4…〔外〕 |
| 85 | b675aff8_by_fStikBot_85_🎧.webp | image/png | 251x256 | 187.2 | sha256:213846ddce3de12d…〔外〕 |
| 86 | b675aff8_by_fStikBot_86_🤯.webp | image/png | 256x250 | 222.9 | sha256:36d5864b27f88404…〔外〕 |
| 87 | b675aff8_by_fStikBot_87_🔫.webp | image/png | 256x256 | 274.2 | sha256:a22a658cec77d16f…〔外〕 |
| 88 | b675aff8_by_fStikBot_88_🌟.webp | image/png | 256x173 | 92.2 | sha256:f581d47457a5b9db…〔外〕 |
| 89 | b675aff8_by_fStikBot_89_🌟.webp | image/png | 194x256 | 267.2 | sha256:80518ddc9b631ecc…〔外〕 |
| 90 | b675aff8_by_fStikBot_8_👍.webp | image/png | 256x256 | 44.2 | sha256:dd69c04a89b3ffbc…〔外〕 |
| 91 | b675aff8_by_fStikBot_90_🌟.webp | image/png | 256x188 | 202.6 | sha256:7eb17707427e7c17…〔外〕 |
| 92 | b675aff8_by_fStikBot_91_🌟.webp | image/png | 256x248 | 93.8 | sha256:8fca23d624ed1bad…〔外〕 |
| 93 | b675aff8_by_fStikBot_92_🌟.webp | image/png | 246x256 | 137.8 | sha256:2d6a85614b9d3056…〔外〕 |
| 94 | b675aff8_by_fStikBot_93_🌟.webp | image/png | 256x256 | 181.8 | sha256:63444681fe208bbe…〔外〕 |
| 95 | b675aff8_by_fStikBot_94_🌟.webp | image/png | 256x238 | 128.0 | sha256:61a50669316023df…〔外〕 |
| 96 | b675aff8_by_fStikBot_95_🖼️.webp | image/png | 194x256 | 261.4 | sha256:2b844f333dc95b5c…〔外〕 |
| 97 | b675aff8_by_fStikBot_96_🌟.webp | image/png | 256x210 | 253.8 | sha256:9063ff829fe160d2…〔外〕 |
| 98 | b675aff8_by_fStikBot_97_🖼️.webp | image/png | 256x206 | 200.0 | sha256:9d968be15ec0ff72…〔外〕 |
| 99 | b675aff8_by_fStikBot_98_🌟.webp | image/png | 256x230 | 305.2 | sha256:4d49b0e95c949f2a…〔外〕 |
| 100 | b675aff8_by_fStikBot_99_🌟.webp | image/png | 256x73 | 118.4 | sha256:7be9c2b4f9372c7a…〔外〕 |
| 101 | b675aff8_by_fStikBot_9_😃.webp | image/png | 256x167 | 114.1 | sha256:b7a09cfa4362affa…〔外〕 |


## 13. `kirinfav_by_favorite_stickers_bot` — `kirinfav_by_favorite_stickers_bot.json`

- 標題:`kirinfav_by_favorite_stickers_bot`;包 ID:`kirinfav_by_favorite_stickers_bot`
- 張數:120;mimetype 分佈:image/png ×120
- 大小統計:合計 23,432,667 B(22.35 MB);平均 190.7 KB;最小 36.7 KB;最大 447.1 KB
- 來源 ID:sha256(外) ×120(全包皆為外部匯入條目)

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | kirinfav_by_favorite_stickers_bot_100_🌟.webp | image/png | 256x256 | 307.7 | sha256:38d2af1bdd0827cb…〔外〕 |
| 2 | kirinfav_by_favorite_stickers_bot_101_😰.webp | image/png | 256x221 | 212.8 | sha256:97436d9c44b38f2b…〔外〕 |
| 3 | kirinfav_by_favorite_stickers_bot_102_🌟.webp | image/png | 256x248 | 146.8 | sha256:ccf6f8f8d63d35f5…〔外〕 |
| 4 | kirinfav_by_favorite_stickers_bot_103_🌟.webp | image/png | 252x256 | 203.9 | sha256:eda1fbdd444f5358…〔外〕 |
| 5 | kirinfav_by_favorite_stickers_bot_104_🐱.webp | image/png | 256x256 | 276.4 | sha256:a42728848d95169e…〔外〕 |
| 6 | kirinfav_by_favorite_stickers_bot_105_🤷‍♀️.webp | image/png | 256x128 | 84.0 | sha256:d21aa705de38ea2f…〔外〕 |
| 7 | kirinfav_by_favorite_stickers_bot_106_🦊.webp | image/png | 256x128 | 70.7 | sha256:a95fc0802525485c…〔外〕 |
| 8 | kirinfav_by_favorite_stickers_bot_107_🙌.webp | image/png | 256x128 | 74.9 | sha256:e75d868a6f65ec71…〔外〕 |
| 9 | kirinfav_by_favorite_stickers_bot_108_😵.webp | image/png | 256x128 | 79.4 | sha256:6d8cc4e91091f64c…〔外〕 |
| 10 | kirinfav_by_favorite_stickers_bot_109_😵.webp | image/png | 256x128 | 78.3 | sha256:824216bd49b7bc25…〔外〕 |
| 11 | kirinfav_by_favorite_stickers_bot_10_☠.webp | image/png | 210x256 | 283.1 | sha256:58a140b64b62bac0…〔外〕 |
| 12 | kirinfav_by_favorite_stickers_bot_110_🤪.webp | image/png | 256x256 | 183.0 | sha256:be68274ca33b7a9f…〔外〕 |
| 13 | kirinfav_by_favorite_stickers_bot_111_✋.webp | image/png | 256x229 | 121.1 | sha256:775e64a9bc111826…〔外〕 |
| 14 | kirinfav_by_favorite_stickers_bot_112_😅.webp | image/png | 254x256 | 344.5 | sha256:f40e9aea84254549…〔外〕 |
| 15 | kirinfav_by_favorite_stickers_bot_113_🧠.webp | image/png | 256x256 | 314.4 | sha256:d8048088a649b49a…〔外〕 |
| 16 | kirinfav_by_favorite_stickers_bot_114_✊.webp | image/png | 256x243 | 279.7 | sha256:be3b86caf76de2f7…〔外〕 |
| 17 | kirinfav_by_favorite_stickers_bot_115_😄.webp | image/png | 256x256 | 182.4 | sha256:dfc0ce96c897d0bc…〔外〕 |
| 18 | kirinfav_by_favorite_stickers_bot_116_🦽.webp | image/png | 256x230 | 69.8 | sha256:1f3e4cab9a714bfc…〔外〕 |
| 19 | kirinfav_by_favorite_stickers_bot_117_🐠.webp | image/png | 256x238 | 59.1 | sha256:4b16fa2f99ddbdda…〔外〕 |
| 20 | kirinfav_by_favorite_stickers_bot_118_🎮.webp | image/png | 256x229 | 125.3 | sha256:d196c6ccdde7d381…〔外〕 |
| 21 | kirinfav_by_favorite_stickers_bot_119_🧨.webp | image/png | 209x256 | 165.1 | sha256:28100ddc5bbb7542…〔外〕 |
| 22 | kirinfav_by_favorite_stickers_bot_11_😄.webp | image/png | 256x256 | 322.5 | sha256:2070298b1764d031…〔外〕 |
| 23 | kirinfav_by_favorite_stickers_bot_120_🥣.webp | image/png | 256x256 | 394.5 | sha256:a39a25b7422672e7…〔外〕 |
| 24 | kirinfav_by_favorite_stickers_bot_12_📄.webp | image/png | 256x234 | 222.1 | sha256:4f16bc22904f4496…〔外〕 |
| 25 | kirinfav_by_favorite_stickers_bot_13_🙂.webp | image/png | 256x256 | 211.0 | sha256:6c38c0cb29803f53…〔外〕 |
| 26 | kirinfav_by_favorite_stickers_bot_14_🤔.webp | image/png | 256x256 | 222.9 | sha256:41162c8fc69886fe…〔外〕 |
| 27 | kirinfav_by_favorite_stickers_bot_15_☺️.webp | image/png | 256x256 | 225.4 | sha256:4580be92cb0e635d…〔外〕 |
| 28 | kirinfav_by_favorite_stickers_bot_16_🤤.webp | image/png | 256x249 | 214.9 | sha256:f363b5df01ac0023…〔外〕 |
| 29 | kirinfav_by_favorite_stickers_bot_17_❓.webp | image/png | 256x256 | 200.1 | sha256:5ea51911fa6202ca…〔外〕 |
| 30 | kirinfav_by_favorite_stickers_bot_18_🤤.webp | image/png | 256x194 | 187.7 | sha256:83b8f60e41b698b5…〔外〕 |
| 31 | kirinfav_by_favorite_stickers_bot_19_😭.webp | image/png | 256x197 | 181.9 | sha256:cebe65f55f45121c…〔外〕 |
| 32 | kirinfav_by_favorite_stickers_bot_1_👋.webp | image/png | 256x256 | 101.0 | sha256:fe80c84c13f43dea…〔外〕 |
| 33 | kirinfav_by_favorite_stickers_bot_20_😄.webp | image/png | 256x189 | 194.8 | sha256:5bfa8308210462d0…〔外〕 |
| 34 | kirinfav_by_favorite_stickers_bot_21_😊.webp | image/png | 256x189 | 185.0 | sha256:e0e10b90b123d131…〔外〕 |
| 35 | kirinfav_by_favorite_stickers_bot_22_👀.webp | image/png | 256x221 | 172.8 | sha256:baf8177c53b2dd91…〔外〕 |
| 36 | kirinfav_by_favorite_stickers_bot_23_😵‍💫.webp | image/png | 244x256 | 209.5 | sha256:2c94ce8c9d007d0a…〔外〕 |
| 37 | kirinfav_by_favorite_stickers_bot_24_😠.webp | image/png | 256x254 | 231.2 | sha256:533820611864c880…〔外〕 |
| 38 | kirinfav_by_favorite_stickers_bot_25_😠.webp | image/png | 252x256 | 228.4 | sha256:a2b61ddd2880b3ba…〔外〕 |
| 39 | kirinfav_by_favorite_stickers_bot_26_😄.webp | image/png | 256x255 | 229.2 | sha256:a458596f1d7bbd7a…〔外〕 |
| 40 | kirinfav_by_favorite_stickers_bot_27_👀.webp | image/png | 256x137 | 125.9 | sha256:062c235d4a67965d…〔外〕 |
| 41 | kirinfav_by_favorite_stickers_bot_28_😩.webp | image/png | 256x256 | 219.7 | sha256:6058711b259871ed…〔外〕 |
| 42 | kirinfav_by_favorite_stickers_bot_29_🖕.webp | image/png | 256x154 | 157.4 | sha256:c326628b72288dca…〔外〕 |
| 43 | kirinfav_by_favorite_stickers_bot_2_👊.webp | image/png | 256x256 | 119.9 | sha256:2b14ce7146de8c00…〔外〕 |
| 44 | kirinfav_by_favorite_stickers_bot_30_😭.webp | image/png | 245x256 | 216.7 | sha256:483cfc964ed6b1d2…〔外〕 |
| 45 | kirinfav_by_favorite_stickers_bot_31_😵‍💫.webp | image/png | 256x214 | 175.4 | sha256:9a1c45edcc30abb6…〔外〕 |
| 46 | kirinfav_by_favorite_stickers_bot_32_😏.webp | image/png | 252x256 | 218.8 | sha256:f0b9e8f5260831c4…〔外〕 |
| 47 | kirinfav_by_favorite_stickers_bot_33_🍑.webp | image/png | 256x208 | 144.5 | sha256:1c63564f071d0991…〔外〕 |
| 48 | kirinfav_by_favorite_stickers_bot_34_🌸.webp | image/png | 256x256 | 187.7 | sha256:386629af271bb43e…〔外〕 |
| 49 | kirinfav_by_favorite_stickers_bot_35_🌸.webp | image/png | 256x256 | 191.3 | sha256:bf17488ae1055112…〔外〕 |
| 50 | kirinfav_by_favorite_stickers_bot_36_🌸.webp | image/png | 256x256 | 183.6 | sha256:75b7172dfe566ef2…〔外〕 |
| 51 | kirinfav_by_favorite_stickers_bot_37_🌸.webp | image/png | 256x256 | 144.0 | sha256:3f855414de40fa35…〔外〕 |
| 52 | kirinfav_by_favorite_stickers_bot_38_😫.webp | image/png | 256x256 | 447.1 | sha256:9f3a140294acc286…〔外〕 |
| 53 | kirinfav_by_favorite_stickers_bot_39_😫.webp | image/png | 245x256 | 240.5 | sha256:52b8e5db7373ce9d…〔外〕 |
| 54 | kirinfav_by_favorite_stickers_bot_3_😐.webp | image/png | 253x256 | 208.9 | sha256:772ad36ff6409380…〔外〕 |
| 55 | kirinfav_by_favorite_stickers_bot_40_😋.webp | image/png | 256x200 | 160.9 | sha256:76fadf6c06ce1ad6…〔外〕 |
| 56 | kirinfav_by_favorite_stickers_bot_41_😁.webp | image/png | 256x203 | 169.0 | sha256:dbbcd80d80b4d2aa…〔外〕 |
| 57 | kirinfav_by_favorite_stickers_bot_42_🛏️.webp | image/png | 255x256 | 251.2 | sha256:a36d8be1e39a371e…〔外〕 |
| 58 | kirinfav_by_favorite_stickers_bot_43_🚫.webp | image/png | 256x256 | 179.2 | sha256:f1b77f6f0688db94…〔外〕 |
| 59 | kirinfav_by_favorite_stickers_bot_44_😊.webp | image/png | 256x256 | 176.6 | sha256:36931c0545511e5f…〔外〕 |
| 60 | kirinfav_by_favorite_stickers_bot_45_😶.webp | image/png | 256x256 | 176.5 | sha256:f31beca6c37808d5…〔外〕 |
| 61 | kirinfav_by_favorite_stickers_bot_46_🙄.webp | image/png | 256x256 | 231.6 | sha256:9d8a48ef0e5937e9…〔外〕 |
| 62 | kirinfav_by_favorite_stickers_bot_47_😶.webp | image/png | 256x256 | 169.1 | sha256:aedc09697ea87966…〔外〕 |
| 63 | kirinfav_by_favorite_stickers_bot_48_😶.webp | image/png | 256x256 | 201.7 | sha256:14e48340363652f0…〔外〕 |
| 64 | kirinfav_by_favorite_stickers_bot_49_😄.webp | image/png | 256x252 | 304.7 | sha256:e6d66bbc85d05073…〔外〕 |
| 65 | kirinfav_by_favorite_stickers_bot_4_😊.webp | image/png | 253x256 | 189.4 | sha256:217480cb2427ab91…〔外〕 |
| 66 | kirinfav_by_favorite_stickers_bot_50_😄.webp | image/png | 256x256 | 230.9 | sha256:c20ba5a3f123c0b6…〔外〕 |
| 67 | kirinfav_by_favorite_stickers_bot_51_👉.webp | image/png | 238x256 | 227.0 | sha256:5a030d21aa71360d…〔外〕 |
| 68 | kirinfav_by_favorite_stickers_bot_52_😳.webp | image/png | 256x218 | 153.4 | sha256:93e2c0486383cb89…〔外〕 |
| 69 | kirinfav_by_favorite_stickers_bot_53_🚪.webp | image/png | 256x222 | 252.1 | sha256:5f0dd255d5fc3030…〔外〕 |
| 70 | kirinfav_by_favorite_stickers_bot_54_0⃣.webp | image/png | 256x239 | 145.7 | sha256:7996bc1ee9503aaf…〔外〕 |
| 71 | kirinfav_by_favorite_stickers_bot_55_🌟.webp | image/png | 237x256 | 234.8 | sha256:b6608fc6f642f2d9…〔外〕 |
| 72 | kirinfav_by_favorite_stickers_bot_56_😤.webp | image/png | 256x178 | 137.6 | sha256:e4fc4c2000f74506…〔外〕 |
| 73 | kirinfav_by_favorite_stickers_bot_57_🤔.webp | image/png | 256x94 | 36.7 | sha256:184260a2f8e8785b…〔外〕 |
| 74 | kirinfav_by_favorite_stickers_bot_58_😆.webp | image/png | 256x134 | 61.9 | sha256:91a28dea4e622859…〔外〕 |
| 75 | kirinfav_by_favorite_stickers_bot_59_😒.webp | image/png | 181x256 | 109.2 | sha256:7a09ebf1e161dace…〔外〕 |
| 76 | kirinfav_by_favorite_stickers_bot_5_🍋.webp | image/png | 256x256 | 181.2 | sha256:fd9b4fb0a9eed62d…〔外〕 |
| 77 | kirinfav_by_favorite_stickers_bot_60_😏.webp | image/png | 181x256 | 107.9 | sha256:2aae15b28861cd1c…〔外〕 |
| 78 | kirinfav_by_favorite_stickers_bot_61_🤮.webp | image/png | 256x188 | 156.5 | sha256:66a57a28c085d5ff…〔外〕 |
| 79 | kirinfav_by_favorite_stickers_bot_62_😁.webp | image/png | 256x256 | 217.4 | sha256:c68517538501f011…〔外〕 |
| 80 | kirinfav_by_favorite_stickers_bot_63_🚬.webp | image/png | 256x141 | 117.3 | sha256:7df1c39ca7a33903…〔外〕 |
| 81 | kirinfav_by_favorite_stickers_bot_64_👈.webp | image/png | 256x256 | 115.2 | sha256:fdef19814fce8dfc…〔外〕 |
| 82 | kirinfav_by_favorite_stickers_bot_65_🉑.webp | image/png | 219x256 | 150.8 | sha256:7ce4ce7114139ea7…〔外〕 |
| 83 | kirinfav_by_favorite_stickers_bot_66_😒.webp | image/png | 256x184 | 102.9 | sha256:b8d17cf147832447…〔外〕 |
| 84 | kirinfav_by_favorite_stickers_bot_67_🤔.webp | image/png | 256x256 | 193.3 | sha256:d2a67847f9e4d7b4…〔外〕 |
| 85 | kirinfav_by_favorite_stickers_bot_68_😊.webp | image/png | 256x256 | 174.4 | sha256:bbf02a5e4165d5a6…〔外〕 |
| 86 | kirinfav_by_favorite_stickers_bot_69_😢.webp | image/png | 256x240 | 208.5 | sha256:e8fe609b10ac7432…〔外〕 |
| 87 | kirinfav_by_favorite_stickers_bot_6_😌.webp | image/png | 256x256 | 308.3 | sha256:a07a15fd758020d9…〔外〕 |
| 88 | kirinfav_by_favorite_stickers_bot_70_🌝.webp | image/png | 223x256 | 152.1 | sha256:4f33ae5765281ec5…〔外〕 |
| 89 | kirinfav_by_favorite_stickers_bot_71_🌝.webp | image/png | 226x256 | 143.3 | sha256:825742f581f5512b…〔外〕 |
| 90 | kirinfav_by_favorite_stickers_bot_72_😶.webp | image/png | 229x256 | 159.5 | sha256:565656365ba381bf…〔外〕 |
| 91 | kirinfav_by_favorite_stickers_bot_73_😂.webp | image/png | 200x256 | 148.3 | sha256:1e7ade0d5ff81766…〔外〕 |
| 92 | kirinfav_by_favorite_stickers_bot_74_👍.webp | image/png | 256x167 | 147.8 | sha256:312555cd0c5d060d…〔外〕 |
| 93 | kirinfav_by_favorite_stickers_bot_75_🐴.webp | image/png | 256x256 | 200.1 | sha256:04ec935575ce8de0…〔外〕 |
| 94 | kirinfav_by_favorite_stickers_bot_76_🐦.webp | image/png | 255x256 | 270.0 | sha256:ecbc8dc063c82292…〔外〕 |
| 95 | kirinfav_by_favorite_stickers_bot_77_🥺.webp | image/png | 200x256 | 129.6 | sha256:bef5711db4eca68a…〔外〕 |
| 96 | kirinfav_by_favorite_stickers_bot_78_😌.webp | image/png | 256x159 | 128.3 | sha256:a11aa047b1885928…〔外〕 |
| 97 | kirinfav_by_favorite_stickers_bot_79_😒.webp | image/png | 256x221 | 291.8 | sha256:485a1b17cfa9215f…〔外〕 |
| 98 | kirinfav_by_favorite_stickers_bot_7_🤤.webp | image/png | 240x256 | 250.5 | sha256:22f03191846d4ea3…〔外〕 |
| 99 | kirinfav_by_favorite_stickers_bot_80_😄.webp | image/png | 222x256 | 266.0 | sha256:b3a1ccb6008a7e58…〔外〕 |
| 100 | kirinfav_by_favorite_stickers_bot_81_😄.webp | image/png | 214x256 | 289.8 | sha256:1aaba27f44949630…〔外〕 |
| 101 | kirinfav_by_favorite_stickers_bot_82_😄.webp | image/png | 214x256 | 285.0 | sha256:72ca0a7e59a885ae…〔外〕 |
| 102 | kirinfav_by_favorite_stickers_bot_83_🤓.webp | image/png | 256x128 | 57.7 | sha256:24d4d654aa4f3ea2…〔外〕 |
| 103 | kirinfav_by_favorite_stickers_bot_84_🤷.webp | image/png | 211x256 | 220.4 | sha256:e0d13ba9ccc15638…〔外〕 |
| 104 | kirinfav_by_favorite_stickers_bot_85_😮.webp | image/png | 256x256 | 203.5 | sha256:737a1e0de120265f…〔外〕 |
| 105 | kirinfav_by_favorite_stickers_bot_86_😑.webp | image/png | 256x229 | 198.0 | sha256:57958d9b3ce0d96a…〔外〕 |
| 106 | kirinfav_by_favorite_stickers_bot_87_🎒.webp | image/png | 234x256 | 220.6 | sha256:d5dc688ea482eba3…〔外〕 |
| 107 | kirinfav_by_favorite_stickers_bot_88_💼.webp | image/png | 234x256 | 220.2 | sha256:88cc2a17efbdebc1…〔外〕 |
| 108 | kirinfav_by_favorite_stickers_bot_89_💖.webp | image/png | 256x256 | 174.4 | sha256:c2246db3b8bc0577…〔外〕 |
| 109 | kirinfav_by_favorite_stickers_bot_8_😅.webp | image/png | 210x256 | 181.6 | sha256:acf0f83a3b3d3d29…〔外〕 |
| 110 | kirinfav_by_favorite_stickers_bot_90_⭐.webp | image/png | 251x256 | 293.2 | sha256:4c79b06404448cf0…〔外〕 |
| 111 | kirinfav_by_favorite_stickers_bot_91_😫.webp | image/png | 256x256 | 118.9 | sha256:24cd0125186da03b…〔外〕 |
| 112 | kirinfav_by_favorite_stickers_bot_92_❓.webp | image/png | 256x256 | 267.7 | sha256:c5e5953e3449b2e4…〔外〕 |
| 113 | kirinfav_by_favorite_stickers_bot_93_🌿.webp | image/png | 256x256 | 64.8 | sha256:0390c680c3a68341…〔外〕 |
| 114 | kirinfav_by_favorite_stickers_bot_94_💣.webp | image/png | 256x184 | 168.1 | sha256:949fa8a45e1fe217…〔外〕 |
| 115 | kirinfav_by_favorite_stickers_bot_95_💣.webp | image/png | 256x184 | 166.7 | sha256:e59d9fd726c353ce…〔外〕 |
| 116 | kirinfav_by_favorite_stickers_bot_96_🌟.webp | image/png | 256x210 | 236.7 | sha256:a48885b5f1c5a244…〔外〕 |
| 117 | kirinfav_by_favorite_stickers_bot_97_🎭.webp | image/png | 256x178 | 195.9 | sha256:540d9ab2e41a0db6…〔外〕 |
| 118 | kirinfav_by_favorite_stickers_bot_98_🌟.webp | image/png | 256x248 | 129.6 | sha256:511271a82ea8f0ce…〔外〕 |
| 119 | kirinfav_by_favorite_stickers_bot_99_🌟.webp | image/png | 256x201 | 206.0 | sha256:e47e8239dc670b3f…〔外〕 |
| 120 | kirinfav_by_favorite_stickers_bot_9_😅.webp | image/png | 220x256 | 286.0 | sha256:fa314b4bd18ca786…〔外〕 |


## 14. `YJSNPI_STICKERS` — `yjsnpis.json`

- 標題:`YJSNPI_STICKERS`;包 ID:`tg-665807805910876161`
- 張數:55;mimetype 分佈:image/png ×55
- 大小統計:合計 10,664,130 B(10.17 MB);平均 189.3 KB;最小 105.7 KB;最大 369.9 KB
- 來源 ID:tg- ×55

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 👴 | image/png | 256x191 | 132.9 | tg-665807805910876201 |
| 2 | 😪 | image/png | 200x256 | 171.5 | tg-665807805910876202 |
| 3 | 🙂 | image/png | 256x256 | 173.2 | tg-665807805910876203 |
| 4 | 🚗 | image/png | 256x256 | 286.5 | tg-665807805910876204 |
| 5 | 😺 | image/png | 256x240 | 137.3 | tg-665807805910876205 |
| 6 | 🌝 | image/png | 256x256 | 250.3 | tg-665807805910876206 |
| 7 | 👓 | image/png | 256x175 | 129.3 | tg-665807805910876207 |
| 8 | 👑 | image/png | 256x150 | 122.3 | tg-665807805910876208 |
| 9 | 😫 | image/png | 256x175 | 109.5 | tg-665807805910876209 |
| 10 | 💊 | image/png | 175x256 | 302.3 | tg-665807805910876210 |
| 11 | 😐 | image/png | 225x256 | 110.9 | tg-665807805910876211 |
| 12 | 🤔 | image/png | 200x256 | 112.2 | tg-665807805910876212 |
| 13 | 😒 | image/png | 240x256 | 157.6 | tg-665807805910876213 |
| 14 | ↗ | image/png | 256x175 | 261.5 | tg-665807805910876214 |
| 15 | 😢 | image/png | 256x160 | 136.0 | tg-665807805910876215 |
| 16 | 🔫 | image/png | 256x256 | 133.6 | tg-665807805910876216 |
| 17 | 😏 | image/png | 200x256 | 208.1 | tg-665807805910876217 |
| 18 | 👼 | image/png | 200x256 | 112.3 | tg-665807805910876218 |
| 19 | 🙄 | image/png | 256x225 | 207.0 | tg-665807805910876219 |
| 20 | 🤵 | image/png | 256x190 | 158.5 | tg-665807805910876220 |
| 21 | 😪 | image/png | 256x175 | 223.9 | tg-665807805910876221 |
| 22 | 🎮 | image/png | 256x210 | 239.6 | tg-665807805910876222 |
| 23 | 🐒 | image/png | 240x256 | 181.9 | tg-665807805910876223 |
| 24 | 💧 | image/png | 256x165 | 166.2 | tg-665807805910876224 |
| 25 | 👨 | image/png | 256x256 | 285.0 | tg-665807805910876225 |
| 26 | ❗ | image/png | 256x150 | 105.7 | tg-665807805910876226 |
| 27 | 🍶 | image/png | 256x190 | 348.7 | tg-665807805910876227 |
| 28 | 😒 | image/png | 165x256 | 145.8 | tg-665807805910876228 |
| 29 | 😫 | image/png | 256x215 | 195.1 | tg-665807805910876229 |
| 30 | ❓ | image/png | 256x175 | 135.5 | tg-665807805910876230 |
| 31 | 😳 | image/png | 256x256 | 203.9 | tg-665807805910876231 |
| 32 | 👨 | image/png | 256x256 | 352.5 | tg-665807805910876232 |
| 33 | ❤ | image/png | 256x190 | 239.8 | tg-665807805910876317 |
| 34 | 🙆 | image/png | 256x256 | 196.5 | tg-665807805910876318 |
| 35 | 😆 | image/png | 256x256 | 202.6 | tg-665807805910876319 |
| 36 | 😄 | image/png | 256x256 | 188.7 | tg-665807805910876320 |
| 37 | 😄 | image/png | 256x256 | 123.8 | tg-665807805910876321 |
| 38 | 😀 | image/png | 256x256 | 135.4 | tg-665807805910876322 |
| 39 | 👱 | image/png | 256x256 | 134.5 | tg-665807805910876323 |
| 40 | 😃 | image/png | 256x256 | 223.6 | tg-665807805910876324 |
| 41 | 🐒 | image/png | 256x256 | 255.0 | tg-665807805910876325 |
| 42 | 🙅 | image/png | 256x256 | 172.9 | tg-665807805910876326 |
| 43 | 😥 | image/png | 256x160 | 193.5 | tg-665807805910876327 |
| 44 | 😧 | image/png | 256x175 | 162.2 | tg-665807805910876328 |
| 45 | 🎮 | image/png | 256x256 | 136.0 | tg-665807805910876329 |
| 46 | 🕵 | image/png | 256x190 | 369.9 | tg-665807805910876330 |
| 47 | 😏 | image/png | 256x256 | 186.6 | tg-665807805910876331 |
| 48 | 🕷 | image/png | 256x256 | 242.4 | tg-665807805910876332 |
| 49 | 👨 | image/png | 256x160 | 165.5 | tg-665807805910876333 |
| 50 | 🔫 | image/png | 256x190 | 194.2 | tg-665807805910876334 |
| 51 | 💥 | image/png | 256x140 | 179.6 | tg-665807805910876335 |
| 52 | 🔫 | image/png | 256x150 | 124.9 | tg-665807805910876336 |
| 53 | 😩 | image/png | 256x256 | 253.1 | tg-665807805910876337 |
| 54 | 🕺 | image/png | 256x200 | 195.7 | tg-665807805910876338 |
| 55 | 😫 | image/png | 256x215 | 141.0 | tg-665807805910876339 |


## 15. `lmao` — `lmao9685.json`

- 標題:`lmao`;包 ID:`tg-5335452775897628671`
- 張數:66;mimetype 分佈:image/png ×66
- 大小統計:合計 7,474,903 B(7.13 MB);平均 110.6 KB;最小 43.1 KB;最大 366.7 KB
- 來源 ID:tg- ×66

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🤦‍♀️ | image/png | 116x256 | 92.4 | tg-6116060852870191766 |
| 2 | 🧦 | image/png | 244x256 | 206.6 | tg-6116443324002869246 |
| 3 | 😒 | image/png | 189x256 | 366.7 | tg-6116098116006461860 |
| 4 | 💀 | image/png | 189x256 | 358.0 | tg-6115977122482756683 |
| 5 | 💀 | image/png | 256x256 | 137.0 | tg-6116022541761910794 |
| 6 | 👩 | image/png | 240x256 | 126.0 | tg-6116417811897129861 |
| 7 | 📦 | image/png | 256x256 | 187.9 | tg-6129926360216380594 |
| 8 | 🫰 | image/png | 256x154 | 65.3 | tg-6131846700223962546 |
| 9 | 🕚 | image/png | 256x202 | 89.8 | tg-6129526825178635257 |
| 10 | 💜 | image/png | 256x155 | 70.1 | tg-6129774266834492519 |
| 11 | 🪤 | image/png | 256x133 | 61.5 | tg-6132202117357641028 |
| 12 | 👩‍👩‍👦‍👦 | image/png | 256x155 | 79.4 | tg-6131819964052545125 |
| 13 | 👨‍🚒 | image/png | 256x133 | 62.2 | tg-6131746893773938712 |
| 14 | 🕵‍♂️ | image/png | 256x134 | 62.6 | tg-6131948224660905748 |
| 15 | 🪒 | image/png | 256x133 | 53.6 | tg-6131815591775838380 |
| 16 | 💇‍♀️ | image/png | 256x190 | 89.6 | tg-6131966933538446856 |
| 17 | 🙅 | image/png | 256x143 | 63.2 | tg-6132142868283791825 |
| 18 | 🤸‍♂️ | image/png | 241x256 | 110.0 | tg-6131685389842258729 |
| 19 | ⛔ | image/png | 256x111 | 50.2 | tg-6136401873818623080 |
| 20 | 👩‍🦽 | image/png | 256x108 | 87.9 | tg-6138565455004048184 |
| 21 | 😇 | image/png | 170x256 | 118.8 | tg-6140956519132307391 |
| 22 | 👢 | image/png | 256x143 | 66.9 | tg-6145498129220246221 |
| 23 | 👩‍❤️‍👩 | image/png | 256x155 | 72.0 | tg-6145326107190106649 |
| 24 | 👍 | image/png | 256x256 | 132.3 | tg-6147533501336918824 |
| 25 | 🇵🇼 | image/png | 183x256 | 114.2 | tg-6152472494683987335 |
| 26 | 🛰️ | image/png | 256x148 | 67.5 | tg-6154362928834290256 |
| 27 | 🩰 | image/png | 253x256 | 95.5 | tg-6161283972279049826 |
| 28 | 👨‍🦳 | image/png | 256x207 | 85.8 | tg-6167858162754919757 |
| 29 | ☕ | image/png | 256x168 | 87.5 | tg-6172647025520155917 |
| 30 | 🕵️‍♀️ | image/png | 256x102 | 49.4 | tg-6172219951152110461 |
| 31 | 🙈 | image/png | 256x175 | 85.2 | tg-6172259752614043696 |
| 32 | 🐅 | image/png | 256x227 | 132.8 | tg-6172533591138900790 |
| 33 | 👨‍🤝‍👨 | image/png | 256x163 | 90.5 | tg-6172345200988397421 |
| 34 | 🧑‍🌾 | image/png | 200x256 | 231.8 | tg-6188189897984058973 |
| 35 | 👨‍❤️‍👨 | image/png | 256x96 | 48.5 | tg-6188391482274094884 |
| 36 | 👍 | image/png | 256x256 | 59.1 | tg-6192968444237847576 |
| 37 | 🤵‍♂️ | image/png | 256x184 | 115.9 | tg-6192533385525599422 |
| 38 | 🙆‍♀️ | image/png | 256x100 | 43.1 | tg-6192584298067925651 |
| 39 | 👍 | image/png | 256x256 | 151.5 | tg-6195042007203716086 |
| 40 | 👍 | image/png | 256x256 | 166.5 | tg-6195051834088890223 |
| 41 | 👍 | image/png | 256x256 | 124.0 | tg-6215011208538364870 |
| 42 | 👍 | image/png | 256x256 | 152.1 | tg-6213214344545574389 |
| 43 | 👍 | image/png | 256x256 | 88.7 | tg-6215308166872178368 |
| 44 | 🙇‍♀️ | image/png | 256x176 | 74.5 | tg-6240053019652661252 |
| 45 | 🖤 | image/png | 256x134 | 99.0 | tg-6251385114769497810 |
| 46 | 🫂 | image/png | 256x113 | 88.7 | tg-6249250851030834736 |
| 47 | 💜 | image/png | 256x194 | 94.4 | tg-6258050135213743169 |
| 48 | ⛹‍♂️ | image/png | 256x146 | 69.1 | tg-6296270868792221393 |
| 49 | 🇨🇨 | image/png | 191x256 | 84.5 | tg-6323198179139394652 |
| 50 | 🚷 | image/png | 256x190 | 89.8 | tg-6323402031172164513 |
| 51 | 👩‍🏭 | image/png | 256x190 | 75.7 | tg-6323444886355844494 |
| 52 | 👍 | image/png | 256x112 | 46.0 | tg-6323362633437158935 |
| 53 | 👍 | image/png | 256x256 | 143.1 | tg-6053124553893224417 |
| 54 | 🖼 | image/png | 256x256 | 111.8 | tg-6057493802648607714 |
| 55 | 👍 | image/png | 256x256 | 247.4 | tg-6057770475851883325 |
| 56 | 👩‍🦳 | image/png | 86x256 | 63.4 | tg-6116370876494520314 |
| 57 | 💆‍♀️ | image/png | 256x159 | 83.1 | tg-6118670401984798378 |
| 58 | 👩‍❤️‍💋‍👩 | image/png | 256x200 | 78.8 | tg-6116170988716564199 |
| 59 | 🙍‍♂️ | image/png | 256x156 | 105.0 | tg-6118499848833474002 |
| 60 | 👍 | image/png | 256x256 | 198.5 | tg-6188021247503248460 |
| 61 | 🖼 | image/png | 256x256 | 74.7 | tg-6192536482197018992 |
| 62 | 🖼 | image/png | 256x256 | 79.6 | tg-6192772404750590268 |
| 63 | 👍 | image/png | 256x256 | 220.3 | tg-6244439723155136659 |
| 64 | 👍 | image/png | 256x256 | 164.2 | tg-6248861417756172354 |
| 65 | 🫶 | image/png | 256x230 | 121.5 | tg-6249304976208700190 |
| 66 | 📗 | image/png | 256x183 | 87.2 | tg-6284982041175926072 |


## 16. `不关猫猫的事哦 @moonrenddev` — `wuyuan5.json`

- 標題:`不关猫猫的事哦 @moonrenddev`;包 ID:`tg-8805721531431780354`
- 張數:23;mimetype 分佈:image/png ×23
- 大小統計:合計 4,615,686 B(4.40 MB);平均 196.0 KB;最小 46.9 KB;最大 455.0 KB
- 來源 ID:tg- ×23

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🏳 | image/png | 256x256 | 213.9 | tg-6248994793670584096 |
| 2 | 🚹 | image/png | 256x256 | 192.7 | tg-6251426698642858077 |
| 3 | 👎 | image/png | 256x256 | 46.9 | tg-6248829467494456591 |
| 4 | 🐦 | image/png | 256x256 | 211.8 | tg-6251529971131490570 |
| 5 | 🖼 | image/png | 256x256 | 124.5 | tg-6248809315507904041 |
| 6 | 👍 | image/png | 256x256 | 102.5 | tg-6248827805342115120 |
| 7 | 🧸 | image/png | 256x256 | 384.4 | tg-6249183712102064348 |
| 8 | 📝 | image/png | 256x256 | 95.6 | tg-6249039757683204252 |
| 9 | 🔪 | image/png | 256x256 | 253.3 | tg-6258171506694562698 |
| 10 | 📦 | image/png | 256x256 | 84.9 | tg-6273940869963852610 |
| 11 | 😺 | image/png | 256x256 | 181.7 | tg-6273595369909657264 |
| 12 | 😁 | image/png | 256x256 | 48.9 | tg-6275924869976694724 |
| 13 | 🦈 | image/png | 256x256 | 159.5 | tg-6284873580366801284 |
| 14 | 📖 | image/png | 256x256 | 455.0 | tg-6285311091505374389 |
| 15 | 😰 | image/png | 256x256 | 256.8 | tg-6284876642678481915 |
| 16 | 👄 | image/png | 256x256 | 140.1 | tg-6293790477934141752 |
| 17 | 🐳 | image/png | 256x256 | 305.3 | tg-6298699251891315405 |
| 18 | 🦈 | image/png | 256x256 | 244.7 | tg-6298585830394961863 |
| 19 | 🔥 | image/png | 256x256 | 90.9 | tg-6309838833689042571 |
| 20 | 🙏 | image/png | 256x256 | 222.3 | tg-6336692257713823936 |
| 21 | 💊 | image/png | 256x256 | 259.9 | tg-6337114474473857858 |
| 22 | 🍉 | image/png | 256x256 | 228.0 | tg-6336618199592739687 |
| 23 | ☠ | image/png | 256x256 | 204.2 | tg-6062132118220185970 |


## 17. `Gay?  @Ali_Yhyee_st` — `GayPackbyAli_yhyee.json`

- 標題:`Gay?  @Ali_Yhyee_st`;包 ID:`tg-1926323992243732493`
- 張數:30;mimetype 分佈:image/png ×30
- 大小統計:合計 3,309,901 B(3.16 MB);平均 107.7 KB;最小 82.6 KB;最大 126.2 KB
- 來源 ID:tg- ×30

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 👋 | image/png | 256x256 | 89.2 | tg-1926323992243733042 |
| 2 | 👋 | image/png | 256x256 | 91.9 | tg-1926323992243733043 |
| 3 | 😍 | image/png | 256x256 | 102.5 | tg-1926323992243733044 |
| 4 | 😕 | image/png | 256x256 | 100.8 | tg-1926323992243733045 |
| 5 | 😉 | image/png | 256x256 | 93.8 | tg-1926323992243733046 |
| 6 | 🙄 | image/png | 256x256 | 102.2 | tg-1926323992243733047 |
| 7 | 😑 | image/png | 256x256 | 126.2 | tg-1926323992243733048 |
| 8 | 😐 | image/png | 256x256 | 114.1 | tg-1926323992243733049 |
| 9 | 😑 | image/png | 256x256 | 118.1 | tg-1926323992243733050 |
| 10 | 🤨 | image/png | 256x256 | 109.1 | tg-1926323992243733051 |
| 11 | 😑 | image/png | 256x256 | 119.7 | tg-1926323992243733052 |
| 12 | 😐 | image/png | 256x256 | 106.1 | tg-1926323992243733053 |
| 13 | 🤨 | image/png | 256x256 | 118.5 | tg-1926323992243733054 |
| 14 | 😒 | image/png | 256x256 | 98.1 | tg-1926323992243733055 |
| 15 | 😐 | image/png | 256x256 | 117.9 | tg-1926323992243733056 |
| 16 | 😐 | image/png | 256x256 | 116.6 | tg-1926323992243733058 |
| 17 | 😐 | image/png | 256x256 | 109.1 | tg-1926323992243733059 |
| 18 | 🤨 | image/png | 256x256 | 115.7 | tg-1926323992243733061 |
| 19 | 😂 | image/png | 256x256 | 114.1 | tg-1926323992243733062 |
| 20 | 😑 | image/png | 256x256 | 82.6 | tg-1926323992243733063 |
| 21 | 🤦‍♂ | image/png | 256x256 | 100.3 | tg-1926323992243733064 |
| 22 | 🤦‍♂ | image/png | 256x256 | 122.9 | tg-1926323992243733065 |
| 23 | 😐 | image/png | 256x256 | 122.4 | tg-1926323992243733066 |
| 24 | 😐 | image/png | 256x256 | 108.9 | tg-1926323992243733067 |
| 25 | 🤔 | image/png | 256x256 | 118.3 | tg-1926323992243733068 |
| 26 | 😂 | image/png | 256x256 | 101.7 | tg-1926323992243733069 |
| 27 | 🤦‍♂ | image/png | 256x256 | 110.0 | tg-1926323992243733070 |
| 28 | 🤨 | image/png | 256x256 | 99.6 | tg-1926323992243733071 |
| 29 | 🙄 | image/png | 256x256 | 109.2 | tg-1926323992243733072 |
| 30 | 🤦‍♂ | image/png | 256x256 | 92.8 | tg-1926323992243733073 |


## 18. `Zakk 変態語錄 :: @fStikBot` — `zakk_is_hentai_by_fStikBot.json`

- 標題:`Zakk 変態語錄 :: @fStikBot`;包 ID:`tg-7477997348958765065`
- 張數:24;mimetype 分佈:image/png ×24
- 大小統計:合計 2,760,088 B(2.63 MB);平均 112.3 KB;最小 54.4 KB;最大 202.7 KB
- 來源 ID:tg- ×24

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🌟 | image/png | 256x132 | 87.6 | tg-6197173797041218581 |
| 2 | 🌟 | image/png | 256x151 | 105.0 | tg-6194837064249253118 |
| 3 | 🌟 | image/png | 256x137 | 84.5 | tg-6195033485988601825 |
| 4 | 🌟 | image/png | 256x117 | 61.7 | tg-6197034223488999249 |
| 5 | 🌟 | image/png | 256x182 | 104.6 | tg-6194748862800863148 |
| 6 | 🌟 | image/png | 256x179 | 123.6 | tg-6194883175018143304 |
| 7 | 🌟 | image/png | 256x134 | 84.9 | tg-6197247399895769427 |
| 8 | 🌟 | image/png | 256x172 | 122.0 | tg-6195148732846055571 |
| 9 | 🌟 | image/png | 256x228 | 127.5 | tg-6197496306135475381 |
| 10 | 🌟 | image/png | 256x98 | 54.4 | tg-6194876195696286538 |
| 11 | 🌟 | image/png | 256x250 | 161.2 | tg-6195183088289456958 |
| 12 | 🌟 | image/png | 177x256 | 149.0 | tg-6197138110157954823 |
| 13 | 🌟 | image/png | 178x256 | 140.0 | tg-6195169769595871228 |
| 14 | 🌟 | image/png | 256x170 | 107.1 | tg-6197422883669549526 |
| 15 | 🌟 | image/png | 255x256 | 168.6 | tg-6194875667415312142 |
| 16 | 🌟 | image/png | 229x256 | 123.5 | tg-6197346995892396258 |
| 17 | 🌟 | image/png | 256x105 | 66.9 | tg-6196988284518801952 |
| 18 | 🌟 | image/png | 199x256 | 178.8 | tg-6195187220047994490 |
| 19 | 🌟 | image/png | 256x145 | 92.5 | tg-6195048286445903824 |
| 20 | 🌟 | image/png | 215x256 | 102.0 | tg-6197072672036233267 |
| 21 | 🌟 | image/png | 256x105 | 61.4 | tg-6197475767601864303 |
| 22 | 🌟 | image/png | 220x256 | 202.7 | tg-6195001475597344345 |
| 23 | 🌟 | image/png | 256x144 | 83.0 | tg-6195174232066891983 |
| 24 | 🌟 | image/png | 256x176 | 102.8 | tg-6219666673914357466 |


## 19. `阿库露 @zhaxia_cn` — `in_AHDBEC_by_NaiDrawBot.json`

- 標題:`阿库露 @zhaxia_cn`;包 ID:`tg-4209876048168352657`
- 張數:64;mimetype 分佈:image/png ×64
- 大小統計:合計 16,137,442 B(15.39 MB);平均 246.2 KB;最小 126.7 KB;最大 334.9 KB
- 來源 ID:tg- ×64

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🍔 | image/png | 256x256 | 227.0 | tg-6073495738396973814 |
| 2 | 🚨 | image/png | 256x256 | 242.9 | tg-6073649004304931349 |
| 3 | 😱 | image/png | 256x256 | 249.0 | tg-6073644984215541391 |
| 4 | 📸 | image/png | 256x256 | 234.8 | tg-6075825285708649248 |
| 5 | 🚫 | image/png | 256x256 | 199.1 | tg-6073359566458851958 |
| 6 | 🍔 | image/png | 256x256 | 216.3 | tg-6073575044968093355 |
| 7 | 👑 | image/png | 256x256 | 217.5 | tg-6073662812624786562 |
| 8 | 👀 | image/png | 256x256 | 219.7 | tg-6073473915668140939 |
| 9 | 🎨 | image/png | 256x256 | 224.0 | tg-6073157148945159717 |
| 10 | 😏 | image/png | 256x256 | 217.4 | tg-6073257118603941732 |
| 11 | 🤗 | image/png | 256x256 | 232.0 | tg-6073475951482640601 |
| 12 | 😤 | image/png | 256x256 | 221.5 | tg-6073137881721870031 |
| 13 | 👀 | image/png | 256x256 | 173.6 | tg-6073510328400876316 |
| 14 | 🍵 | image/png | 256x256 | 212.0 | tg-6073495867245991281 |
| 15 | ❤️ | image/png | 256x256 | 222.4 | tg-6073215569090319561 |
| 16 | 🧱 | image/png | 256x256 | 126.7 | tg-6073228754639918315 |
| 17 | 🛌 | image/png | 256x256 | 144.3 | tg-6197363763444716937 |
| 18 | 🍔 | image/png | 256x256 | 227.3 | tg-6197231787689645739 |
| 19 | 🔓 | image/png | 256x256 | 252.2 | tg-6197384843144205103 |
| 20 | 🚪 | image/png | 256x256 | 250.2 | tg-6197152966449828860 |
| 21 | 🤔 | image/png | 256x256 | 262.7 | tg-6197224486245241616 |
| 22 | ❤️ | image/png | 256x256 | 231.3 | tg-6197329489605694438 |
| 23 | 😡 | image/png | 256x256 | 250.9 | tg-6197505480185615362 |
| 24 | ❤️ | image/png | 256x256 | 221.3 | tg-6197293265851520270 |
| 25 | 🌌 | image/png | 256x256 | 271.2 | tg-6197384426532378153 |
| 26 | 👌 | image/png | 256x256 | 216.9 | tg-6197410952250397753 |
| 27 | 👌 | image/png | 256x256 | 228.1 | tg-6197345411049460993 |
| 28 | 🌾 | image/png | 256x256 | 299.8 | tg-6197450066517563217 |
| 29 | ❤️ | image/png | 256x256 | 233.1 | tg-6197495133609399850 |
| 30 | 👀 | image/png | 256x256 | 202.8 | tg-6197335725898208160 |
| 31 | 👴 | image/png | 256x256 | 320.4 | tg-6197060938185577388 |
| 32 | 👀 | image/png | 256x256 | 235.6 | tg-6197274763132410551 |
| 33 | 🏥 | image/png | 256x256 | 224.8 | tg-6339164118766852617 |
| 34 | 🌡️ | image/png | 256x256 | 218.3 | tg-6053221495600060389 |
| 35 | 😐 | image/png | 256x256 | 237.6 | tg-6053099767636957485 |
| 36 | ❤️ | image/png | 256x256 | 271.9 | tg-6053027268589000742 |
| 37 | 🤗 | image/png | 256x256 | 280.0 | tg-6053184288298374777 |
| 38 | 😮 | image/png | 256x256 | 156.0 | tg-6053297065549632594 |
| 39 | 🔥 | image/png | 256x256 | 326.5 | tg-6053354695420811941 |
| 40 | ❤️ | image/png | 256x256 | 231.5 | tg-6053295377627485893 |
| 41 | ❤️ | image/png | 256x256 | 271.7 | tg-6339061142630962168 |
| 42 | ❤️ | image/png | 256x256 | 219.1 | tg-6052970609380430763 |
| 43 | 👉 | image/png | 256x256 | 266.6 | tg-6053173636779480498 |
| 44 | 🎭 | image/png | 256x256 | 243.7 | tg-6052967418219731534 |
| 45 | 🙏 | image/png | 256x256 | 243.1 | tg-6053209310777840754 |
| 46 | 🚪 | image/png | 256x256 | 247.3 | tg-6053228401907471363 |
| 47 | 😨 | image/png | 256x256 | 253.4 | tg-6338962899549033938 |
| 48 | 🏥 | image/png | 256x256 | 224.4 | tg-6052990413474632449 |
| 49 | 👴 | image/png | 256x256 | 299.2 | tg-6339363413839321018 |
| 50 | ❤️ | image/png | 256x256 | 303.5 | tg-6339079722659485528 |
| 51 | 🦷 | image/png | 256x256 | 306.6 | tg-6339287878249486332 |
| 52 | 🤔 | image/png | 256x256 | 304.3 | tg-6053076188266502254 |
| 53 | 😨 | image/png | 256x256 | 310.6 | tg-6339207261713341201 |
| 54 | ❤️ | image/png | 256x256 | 309.6 | tg-6339137008933280032 |
| 55 | 👀 | image/png | 256x256 | 334.9 | tg-6052938925406688888 |
| 56 | 👍 | image/png | 256x256 | 267.2 | tg-6052920478522153946 |
| 57 | 📌 | image/png | 256x256 | 281.2 | tg-6339071012465809872 |
| 58 | 🤔 | image/png | 256x256 | 286.0 | tg-6339002185614891849 |
| 59 | 🛁 | image/png | 256x256 | 154.6 | tg-6339329144295266518 |
| 60 | ❤️ | image/png | 256x256 | 288.4 | tg-6339371677356398099 |
| 61 | 🚫 | image/png | 256x256 | 209.2 | tg-6338992367319652350 |
| 62 | 😰 | image/png | 256x256 | 298.1 | tg-6338989983612803739 |
| 63 | 🤚 | image/png | 256x256 | 324.5 | tg-6339131979526576008 |
| 64 | 😰 | image/png | 256x256 | 281.2 | tg-6339202266666375979 |


## 20. `全能表情包#(滑稽)` — `stickersandhuaji.json`

- 標題:`全能表情包#(滑稽)`;包 ID:`tg-1010495870765891586`
- 張數:39;mimetype 分佈:image/png ×39
- 大小統計:合計 6,056,130 B(5.78 MB);平均 151.6 KB;最小 58.4 KB;最大 277.4 KB
- 來源 ID:tg- ×39

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 😏 | image/png | 256x255 | 187.6 | tg-1010495870765891593 |
| 2 | 😊 | image/png | 256x256 | 146.9 | tg-1010495870765891594 |
| 3 | 😅 | image/png | 256x203 | 195.7 | tg-1010495870765891647 |
| 4 | 😝 | image/png | 233x256 | 217.8 | tg-1010495870765891595 |
| 5 | 😆 | image/png | 256x252 | 180.0 | tg-1010495870765891597 |
| 6 | 💏 | image/png | 256x129 | 151.1 | tg-1010495870765891599 |
| 7 | 😠 | image/png | 210x256 | 158.0 | tg-1010495870765891601 |
| 8 | 😡 | image/png | 236x256 | 158.4 | tg-1010495870765891603 |
| 9 | 😋 | image/png | 198x256 | 220.0 | tg-1010495870765891651 |
| 10 | 😶 | image/png | 158x256 | 73.8 | tg-1010495870765891607 |
| 11 | 😌 | image/png | 186x256 | 77.4 | tg-1010495870765891609 |
| 12 | ☺️ | image/png | 170x256 | 58.4 | tg-1010495870765891613 |
| 13 | 😊 | image/png | 203x256 | 105.7 | tg-1010495870765891614 |
| 14 | 🙄 | image/png | 246x256 | 102.1 | tg-1010495870765891616 |
| 15 | 🙈 | image/png | 256x179 | 62.2 | tg-1010495870765891618 |
| 16 | 😕 | image/png | 185x256 | 114.8 | tg-1010495870765891620 |
| 17 | 😜 | image/png | 256x186 | 131.3 | tg-1010495870765891622 |
| 18 | 😲 | image/png | 256x149 | 129.4 | tg-1010495870765891624 |
| 19 | 😒 | image/png | 256x175 | 246.2 | tg-1010495870765891626 |
| 20 | 😛 | image/png | 256x253 | 277.4 | tg-1010495870765891628 |
| 21 | 🌚 | image/png | 256x256 | 188.3 | tg-1010495870765891631 |
| 22 | 😭 | image/png | 256x256 | 197.7 | tg-1010495870765891633 |
| 23 | 😳 | image/png | 256x256 | 124.5 | tg-1010495870765891641 |
| 24 | 🙂 | image/png | 256x256 | 113.9 | tg-1010495870765891635 |
| 25 | 😤 | image/png | 256x256 | 180.6 | tg-1010495870765891673 |
| 26 | 🖐 | image/png | 184x256 | 216.0 | tg-1010495870765891637 |
| 27 | 👀 | image/png | 184x256 | 205.2 | tg-1010495870765891639 |
| 28 | 😐 | image/png | 256x198 | 181.5 | tg-1010495870765891643 |
| 29 | 😂 | image/png | 256x235 | 148.4 | tg-1010495870765891645 |
| 30 | 👍 | image/png | 256x256 | 91.9 | tg-1010495870765891649 |
| 31 | 🐸 | image/png | 256x200 | 271.8 | tg-1010495870765891666 |
| 32 | 😑 | image/png | 244x256 | 99.3 | tg-1010495870765891675 |
| 33 | 🐸 | image/png | 256x198 | 112.2 | tg-1010495870765891677 |
| 34 | 🙊 | image/png | 256x191 | 193.9 | tg-1010495870765891701 |
| 35 | 😐 | image/png | 256x252 | 111.6 | tg-1010495870765891702 |
| 36 | 🐮 | image/png | 256x225 | 172.1 | tg-1010495870765891746 |
| 37 | 🔪 | image/png | 256x230 | 184.7 | tg-1010495870765891747 |
| 38 | 😶 | image/png | 256x118 | 66.5 | tg-1010495870765891748 |
| 39 | 😐 | image/png | 256x128 | 60.0 | tg-1010495870765891749 |


## 21. `s` — `stneng.json`

- 標題:`s`;包 ID:`tg-692497273854099457`
- 張數:28;mimetype 分佈:image/png ×28
- 大小統計:合計 5,540,475 B(5.28 MB);平均 193.2 KB;最小 106.9 KB;最大 343.1 KB
- 來源 ID:tg- ×28

> 註:此前發現的 256x0 畸形貼圖(`tg-692497273854099475`)已自本包摘除;本次編纂重新確認該張未出現於資料中。

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🌚 | image/png | 256x129 | 119.2 | tg-692497273854099467 |
| 2 | 🌚 | image/png | 256x253 | 188.1 | tg-692497273854099472 |
| 3 | 😂 | image/png | 188x256 | 343.1 | tg-692497273854099469 |
| 4 | 😂 | image/png | 256x214 | 180.8 | tg-692497273854099478 |
| 5 | 😱 | image/png | 256x256 | 221.8 | tg-692497273854099468 |
| 6 | 😳 | image/png | 256x232 | 126.2 | tg-692497273854099479 |
| 7 | 😱 | image/png | 256x256 | 299.2 | tg-692497273854099499 |
| 8 | 😅 | image/png | 256x196 | 113.1 | tg-692497273854099501 |
| 9 | 🌚 | image/png | 256x183 | 158.0 | tg-692497273854099477 |
| 10 | 🌚 | image/png | 255x256 | 167.5 | tg-692497273854099480 |
| 11 | 😜 | image/png | 256x125 | 207.4 | tg-692497273854099482 |
| 12 | 😅 | image/png | 256x199 | 167.9 | tg-692497273854099471 |
| 13 | 😉 | image/png | 227x256 | 126.8 | tg-692497273854099473 |
| 14 | 😳 | image/png | 256x113 | 143.5 | tg-692497273854099476 |
| 15 | 😭 | image/png | 209x256 | 136.3 | tg-692497273854099481 |
| 16 | 🌚 | image/png | 256x256 | 151.2 | tg-692497273854099500 |
| 17 | 🌝 | image/png | 139x256 | 111.3 | tg-692497273854099483 |
| 18 | 🌚 | image/png | 249x256 | 277.5 | tg-692497273854099484 |
| 19 | 🌚 | image/png | 235x256 | 261.8 | tg-692497273854099485 |
| 20 | 🌚 | image/png | 248x256 | 287.4 | tg-692497273854099486 |
| 21 | 🌚 | image/png | 248x256 | 281.7 | tg-692497273854099487 |
| 22 | 🌚 | image/png | 250x256 | 283.1 | tg-692497273854099488 |
| 23 | 🤔 | image/png | 256x243 | 120.9 | tg-692497273854099489 |
| 24 | 🤔 | image/png | 256x144 | 187.8 | tg-692497273854099491 |
| 25 | 😱 | image/png | 254x256 | 241.6 | tg-692497273854099492 |
| 26 | 😱 | image/png | 254x256 | 239.9 | tg-692497273854099493 |
| 27 | 😤 | image/png | 256x128 | 106.9 | tg-692497273854099496 |
| 28 | 🤔 | image/png | 256x126 | 160.6 | tg-692497273854099497 |


## 22. `永远怀念` — `ChinaTelecom.json`

- 標題:`永远怀念`;包 ID:`tg-697466963332431876`
- 張數:71;mimetype 分佈:image/png ×71
- 大小統計:合計 4,358,569 B(4.16 MB);平均 59.9 KB;最小 18.3 KB;最大 360.9 KB
- 來源 ID:tg- ×71

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 💩 | image/png | 256x256 | 46.8 | tg-697466963332432425 |
| 2 | 💩 | image/png | 256x256 | 43.4 | tg-697466963332432426 |
| 3 | 💩 | image/png | 256x256 | 110.3 | tg-697466963332432427 |
| 4 | 💩 | image/png | 256x256 | 360.9 | tg-697466963332432428 |
| 5 | 🚵 | image/png | 256x256 | 131.4 | tg-697466963332432429 |
| 6 | 💊 | image/png | 256x256 | 96.2 | tg-697466963332432430 |
| 7 | 💣 | image/png | 256x256 | 48.9 | tg-697466963332432431 |
| 8 | 🕳 | image/png | 256x256 | 43.0 | tg-697466963332432432 |
| 9 | 🎓 | image/png | 256x256 | 42.8 | tg-697466963332432433 |
| 10 | 📚 | image/png | 256x256 | 43.4 | tg-697466963332432434 |
| 11 | ⚡ | image/png | 256x256 | 65.9 | tg-697466963332432435 |
| 12 | 💮 | image/png | 256x256 | 360.9 | tg-697466963332432436 |
| 13 | 👳 | image/png | 256x256 | 356.5 | tg-697466963332432437 |
| 14 | 🚜 | image/png | 256x256 | 26.4 | tg-697466963332432438 |
| 15 | 🌑 | image/png | 256x256 | 42.1 | tg-697466963332432439 |
| 16 | 🎌 | image/png | 256x256 | 28.3 | tg-697466963332432440 |
| 17 | 🚛 | image/png | 256x256 | 24.4 | tg-697466963332432441 |
| 18 | 🚒 | image/png | 256x256 | 41.7 | tg-697466963332432442 |
| 19 | 🚉 | image/png | 256x256 | 28.7 | tg-697466963332432443 |
| 20 | 🚞 | image/png | 256x256 | 22.6 | tg-697466963332432444 |
| 21 | 🍉 | image/png | 256x256 | 29.9 | tg-697466963332432445 |
| 22 | 🍇 | image/png | 256x256 | 24.5 | tg-697466963332432446 |
| 23 | 🍆 | image/png | 256x256 | 24.3 | tg-697466963332432447 |
| 24 | 🍠 | image/png | 256x256 | 30.6 | tg-697466963332432448 |
| 25 | 👘 | image/png | 256x256 | 24.9 | tg-697466963332432449 |
| 26 | 🍭 | image/png | 256x256 | 28.3 | tg-697466963332432450 |
| 27 | 🍯 | image/png | 256x256 | 21.0 | tg-697466963332432451 |
| 28 | 🥐 | image/png | 256x256 | 31.4 | tg-697466963332432452 |
| 29 | 🤷 | image/png | 256x256 | 23.6 | tg-697466963332432453 |
| 30 | 🛶 | image/png | 256x256 | 26.7 | tg-697466963332432454 |
| 31 | 🍶 | image/png | 256x256 | 24.5 | tg-697466963332432455 |
| 32 | 🛴 | image/png | 256x256 | 33.0 | tg-697466963332432456 |
| 33 | 😒 | image/png | 256x256 | 24.0 | tg-697466963332432457 |
| 34 | 🥚 | image/png | 256x256 | 21.0 | tg-697466963332432458 |
| 35 | 🍈 | image/png | 256x256 | 33.7 | tg-697466963332432459 |
| 36 | 💩 | image/png | 256x256 | 41.8 | tg-697466963332432460 |
| 37 | 🌪 | image/png | 256x256 | 45.4 | tg-697466963332432461 |
| 38 | 🌭 | image/png | 256x256 | 25.0 | tg-697466963332432462 |
| 39 | 🥒 | image/png | 256x256 | 35.2 | tg-697466963332432463 |
| 40 | 🍽 | image/png | 256x256 | 23.2 | tg-697466963332432464 |
| 41 | 💥 | image/png | 256x256 | 44.3 | tg-697466963332432465 |
| 42 | 🌚 | image/png | 256x256 | 49.9 | tg-697466963332432466 |
| 43 | 💸 | image/png | 256x84 | 137.9 | tg-697466963332432467 |
| 44 | ☄ | image/png | 256x256 | 27.2 | tg-697466963332432468 |
| 45 | 🌬 | image/png | 256x256 | 18.6 | tg-697466963332432469 |
| 46 | 💩 | image/png | 256x256 | 36.7 | tg-697466963332432470 |
| 47 | 📉 | image/png | 256x256 | 30.2 | tg-697466963332432471 |
| 48 | 💻 | image/png | 256x256 | 22.0 | tg-697466963332432472 |
| 49 | 🚑 | image/png | 256x256 | 18.3 | tg-697466963332432473 |
| 50 | 🦍 | image/png | 256x256 | 27.9 | tg-697466963332432474 |
| 51 | 🔓 | image/png | 256x256 | 51.4 | tg-697466963332432475 |
| 52 | 🔓 | image/png | 256x256 | 23.9 | tg-697466963332432476 |
| 53 | 🐸 | image/png | 256x256 | 33.6 | tg-697466963332432477 |
| 54 | ✈ | image/png | 256x256 | 37.6 | tg-697466963332432478 |
| 55 | ⬛ | image/png | 256x256 | 35.9 | tg-697466963332432479 |
| 56 | 🌊 | image/png | 256x256 | 28.0 | tg-697466963332432480 |
| 57 | 🐔 | image/png | 256x256 | 36.2 | tg-697466963332432481 |
| 58 | 🕵 | image/png | 256x256 | 68.1 | tg-697466963332432482 |
| 59 | 🖼 | image/png | 256x256 | 74.4 | tg-697466963332432483 |
| 60 | 🤝 | image/png | 256x256 | 35.9 | tg-697466963332432485 |
| 61 | 🚶 | image/png | 256x256 | 49.3 | tg-697466963332432486 |
| 62 | 🌞 | image/png | 256x256 | 38.4 | tg-697466963332432487 |
| 63 | ☁ | image/png | 256x256 | 39.5 | tg-697466963332432488 |
| 64 | 🌚 | image/png | 256x256 | 32.2 | tg-697466963332432489 |
| 65 | 🕵 | image/png | 256x256 | 27.7 | tg-697466963332432490 |
| 66 | 💣 | image/png | 256x256 | 54.9 | tg-697466963332432491 |
| 67 | 👻 | image/png | 256x256 | 79.5 | tg-697466963332432492 |
| 68 | 😎 | image/png | 256x256 | 133.5 | tg-697466963332432493 |
| 69 | 🤑 | image/png | 256x256 | 140.3 | tg-697466963332432494 |
| 70 | 😎 | image/png | 256x256 | 142.2 | tg-697466963332432495 |
| 71 | 😎 | image/png | 256x256 | 144.4 | tg-697466963332432496 |


## 23. `Cursed` — `cursedstickerspack_by_favorite_stickers_bot.json`

- 標題:`Cursed`;包 ID:`tg-588290144503595010`
- 張數:78;mimetype 分佈:image/png ×78
- 大小統計:合計 14,807,418 B(14.12 MB);平均 185.4 KB;最小 31.3 KB;最大 379.2 KB
- 來源 ID:tg- ×78

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 😵 | image/png | 256x232 | 164.2 | tg-588290144503595030 |
| 2 | 😫 | image/png | 256x256 | 195.7 | tg-588290144503595031 |
| 3 | 😲 | image/png | 256x81 | 31.3 | tg-588290144503595032 |
| 4 | 😒 | image/png | 256x100 | 102.3 | tg-588290144503595033 |
| 5 | 🚿 | image/png | 192x256 | 224.6 | tg-588290144503595034 |
| 6 | 😂 | image/png | 256x256 | 175.2 | tg-588290144503595035 |
| 7 | 🙃 | image/png | 256x251 | 231.9 | tg-588290144503595036 |
| 8 | 💤 | image/png | 256x249 | 249.5 | tg-588290144503595037 |
| 9 | 🖥 | image/png | 256x255 | 171.7 | tg-588290144503595038 |
| 10 | 😲 | image/png | 245x256 | 229.5 | tg-588290144503595039 |
| 11 | 💁‍♂️ | image/png | 256x255 | 215.5 | tg-588290144503595040 |
| 12 | 😁 | image/png | 239x256 | 202.5 | tg-588290144503595041 |
| 13 | 🤙 | image/png | 219x256 | 154.4 | tg-588290144503595042 |
| 14 | 🙂 | image/png | 256x161 | 109.8 | tg-588290144503595043 |
| 15 | 😏 | image/png | 256x256 | 111.8 | tg-588290144503595044 |
| 16 | 😔 | image/png | 256x192 | 165.1 | tg-588290144503595045 |
| 17 | 💪 | image/png | 256x221 | 71.9 | tg-588290144503595046 |
| 18 | 😅 | image/png | 161x256 | 117.6 | tg-588290144503595047 |
| 19 | 😭 | image/png | 256x233 | 162.1 | tg-588290144503595048 |
| 20 | 👍 | image/png | 256x189 | 107.8 | tg-588290144503595049 |
| 21 | 🙅‍♂ | image/png | 256x128 | 63.6 | tg-588290144503595050 |
| 22 | 🤐 | image/png | 256x238 | 208.3 | tg-588290144503595051 |
| 23 | ❗️ | image/png | 256x247 | 113.9 | tg-588290144503595052 |
| 24 | 😢 | image/png | 256x244 | 229.1 | tg-588290144503595053 |
| 25 | 😓 | image/png | 256x214 | 128.9 | tg-588290144503595055 |
| 26 | 👆 | image/png | 256x256 | 137.5 | tg-588290144503595056 |
| 27 | ☹️ | image/png | 256x128 | 49.3 | tg-588290144503595057 |
| 28 | 😐 | image/png | 256x192 | 133.1 | tg-588290144503595058 |
| 29 | 🥴 | image/png | 256x238 | 174.1 | tg-588290144503595059 |
| 30 | 😦 | image/png | 161x256 | 89.0 | tg-588290144503595060 |
| 31 | 😈 | image/png | 256x165 | 136.7 | tg-588290144503595061 |
| 32 | 😶 | image/png | 256x205 | 118.1 | tg-588290144503595062 |
| 33 | 😶 | image/png | 256x199 | 177.6 | tg-588290144503595063 |
| 34 | 😐 | image/png | 256x165 | 134.1 | tg-588290144503595064 |
| 35 | 👍 | image/png | 256x192 | 137.4 | tg-588290144503595065 |
| 36 | 🐢 | image/png | 256x229 | 197.8 | tg-588290144503595066 |
| 37 | 🔨 | image/png | 256x250 | 201.7 | tg-588290144503595067 |
| 38 | 🐢 | image/png | 193x256 | 325.7 | tg-588290144503595068 |
| 39 | 🤔 | image/png | 256x256 | 219.2 | tg-588290144503595069 |
| 40 | 🤬 | image/png | 231x256 | 237.9 | tg-588290144503595071 |
| 41 | 🤬 | image/png | 245x256 | 209.6 | tg-588290144503595072 |
| 42 | 😕 | image/png | 256x200 | 236.6 | tg-588290144503595073 |
| 43 | 🐦 | image/png | 256x144 | 66.1 | tg-588290144503595074 |
| 44 | 🤮 | image/png | 240x256 | 285.8 | tg-588290144503595075 |
| 45 | 🐦 | image/png | 256x255 | 335.3 | tg-588290144503595076 |
| 46 | 😐 | image/png | 192x256 | 274.2 | tg-588290144503595077 |
| 47 | 👍 | image/png | 256x160 | 181.6 | tg-588290144503595078 |
| 48 | 😐 | image/png | 256x253 | 144.8 | tg-588290144503595079 |
| 49 | 🐶 | image/png | 235x256 | 220.9 | tg-588290144503595080 |
| 50 | 🐦 | image/png | 256x256 | 267.5 | tg-588290144503595081 |
| 51 | 🐦 | image/png | 256x226 | 146.3 | tg-588290144503595082 |
| 52 | 🐦 | image/png | 256x251 | 379.2 | tg-588290144503595083 |
| 53 | 🐦 | image/png | 256x79 | 33.3 | tg-588290144503595084 |
| 54 | 🖕 | image/png | 256x215 | 244.8 | tg-588290144503595085 |
| 55 | 😩 | image/png | 256x256 | 213.5 | tg-588290144503595086 |
| 56 | 🙄 | image/png | 249x256 | 292.1 | tg-588290144503595087 |
| 57 | 🙄 | image/png | 256x222 | 204.0 | tg-588290144503595088 |
| 58 | 🍋 | image/png | 256x144 | 85.4 | tg-588290144503595089 |
| 59 | 🤤 | image/png | 256x256 | 249.2 | tg-588290144503595090 |
| 60 | 😁 | image/png | 256x256 | 186.3 | tg-588290144503595094 |
| 61 | 🤺 | image/png | 256x243 | 235.2 | tg-588290144503595099 |
| 62 | 🤺 | image/png | 256x183 | 203.5 | tg-588290144503595100 |
| 63 | 🤒 | image/png | 256x208 | 181.5 | tg-588290144503595101 |
| 64 | 🥺 | image/png | 256x227 | 185.3 | tg-588290144503595102 |
| 65 | 🏆 | image/png | 256x181 | 309.0 | tg-588290144503595103 |
| 66 | 🕊 | image/png | 256x218 | 139.2 | tg-588290144503595104 |
| 67 | 💸 | image/png | 256x181 | 251.1 | tg-588290144503595105 |
| 68 | 🤯 | image/png | 256x193 | 246.0 | tg-6226585720199316076 |
| 69 | 🏃 | image/png | 254x256 | 163.9 | tg-6264804417963295437 |
| 70 | 👀 | image/png | 256x238 | 272.2 | tg-6100256077595542040 |
| 71 | 📖 | image/png | 256x227 | 340.0 | tg-6183460468976255894 |
| 72 | 🐔 | image/png | 256x199 | 126.8 | tg-6080330753646789382 |
| 73 | 😂 | image/png | 240x256 | 332.2 | tg-6212924481497728587 |
| 74 | 😅 | image/png | 256x169 | 151.3 | tg-6251206749072656094 |
| 75 | 😭 | image/png | 256x256 | 126.8 | tg-6192870944185255604 |
| 76 | 🦠 | image/png | 194x256 | 175.6 | tg-6143438632272267561 |
| 77 | 🙃 | image/png | 256x232 | 188.0 | tg-6192610935455090897 |
| 78 | 😴 | image/png | 256x186 | 169.3 | tg-6217638023421495227 |


## 24. `hfssnpack` — `hfssnpack_by_favorite_stickers_bot.json`

- 標題:`hfssnpack`;包 ID:`tg-3668382827939889151`
- 張數:36;mimetype 分佈:image/png ×36
- 大小統計:合計 7,886,011 B(7.52 MB);平均 213.9 KB;最小 51.7 KB;最大 447.1 KB
- 來源 ID:tg- ×36

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 😅 | image/png | 239x256 | 230.9 | tg-6188088072899397390 |
| 2 | 😋 | image/png | 256x210 | 331.7 | tg-6188506776376182766 |
| 3 | 🤢 | image/png | 256x256 | 296.2 | tg-6188494454115011271 |
| 4 | 🎽 | image/png | 256x198 | 100.7 | tg-6221842152159186459 |
| 5 | 😃 | image/png | 256x256 | 302.5 | tg-6228711076175809972 |
| 6 | 😨 | image/png | 256x256 | 285.1 | tg-6197483008916723272 |
| 7 | 😀 | image/png | 256x256 | 190.0 | tg-6091222176529125105 |
| 8 | 👍 | image/png | 256x256 | 51.7 | tg-6239771046459739844 |
| 9 | ✋ | image/png | 256x256 | 288.4 | tg-6239764329130889373 |
| 10 | 👀 | image/png | 256x256 | 240.8 | tg-6251122043727646204 |
| 11 | 😍 | image/png | 256x256 | 115.6 | tg-6285275486226486000 |
| 12 | ❤ | image/png | 256x256 | 161.9 | tg-6289447200845992031 |
| 13 | 🤨 | image/png | 256x256 | 128.0 | tg-6287089706182120809 |
| 14 | 😫 | image/png | 256x256 | 112.2 | tg-6287317369513580306 |
| 15 | 😱 | image/png | 256x256 | 128.0 | tg-6287166929694103007 |
| 16 | 🎧 | image/png | 256x256 | 138.7 | tg-6289412342891418357 |
| 17 | 😁 | image/png | 256x256 | 110.5 | tg-6289659196136755463 |
| 18 | 😭 | image/png | 256x256 | 338.1 | tg-6300770340956016676 |
| 19 | 😕 | image/png | 256x256 | 134.2 | tg-6314256327812060686 |
| 20 | 🤤 | image/png | 256x256 | 391.0 | tg-6314560926892694057 |
| 21 | 🐱 | image/png | 256x256 | 142.8 | tg-6314402562858556827 |
| 22 | 😮 | image/png | 256x256 | 110.4 | tg-6314261404463405130 |
| 23 | 🧐 | image/png | 256x256 | 338.0 | tg-6156816995837810334 |
| 24 | 🫨 | image/png | 256x256 | 382.2 | tg-6156636804779873458 |
| 25 | 😪 | image/png | 256x256 | 242.9 | tg-6165508055434794772 |
| 26 | 😏 | image/png | 256x256 | 104.5 | tg-6174786249946044646 |
| 27 | 🤚 | image/png | 256x256 | 323.2 | tg-6199566282803648845 |
| 28 | 😝 | image/png | 256x256 | 117.9 | tg-6264752053722026646 |
| 29 | 😁 | image/png | 256x256 | 391.3 | tg-6269142919047812785 |
| 30 | 😈 | image/png | 256x256 | 148.7 | tg-6066696843822110396 |
| 31 | ☺ | image/png | 256x256 | 447.1 | tg-6066641962730001921 |
| 32 | 🥳 | image/png | 256x256 | 183.4 | tg-6239848523374793696 |
| 33 | 😤 | image/png | 256x256 | 214.2 | tg-6215457571604536649 |
| 34 | 😋 | image/png | 256x256 | 192.1 | tg-6215120137498926755 |
| 35 | 🤔 | image/png | 256x256 | 131.6 | tg-6226272956385861277 |
| 36 | 🤬 | image/png | 256x256 | 154.5 | tg-6246908582026026892 |


## 25. `超时空辉夜姬！(XHS:95047506868)` — `CosmicPrincessKaguya1_by_NichistickerBot.json`

- 標題:`超时空辉夜姬！(XHS:95047506868)`;包 ID:`tg-5717016364816793612`
- 張數:36;mimetype 分佈:image/png ×36
- 大小統計:合計 4,686,064 B(4.47 MB);平均 127.1 KB;最小 44.3 KB;最大 249.3 KB
- 來源 ID:tg- ×36

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | ❤️ | image/png | 256x141 | 172.1 | tg-6136632801325227151 |
| 2 | ❤️ | image/png | 253x256 | 208.9 | tg-6116334480941652509 |
| 3 | ❤️ | image/png | 253x256 | 181.2 | tg-6116365400411216234 |
| 4 | ❤️ | image/png | 253x256 | 186.2 | tg-6115973403041079479 |
| 5 | ❤️ | image/png | 256x255 | 249.3 | tg-6215365947067210687 |
| 6 | ❤️ | image/png | 256x240 | 234.0 | tg-6116215553297229810 |
| 7 | ❤️ | image/png | 256x240 | 137.0 | tg-6118253283350947749 |
| 8 | ❤️ | image/png | 256x240 | 141.6 | tg-6116205189541141170 |
| 9 | ❤️ | image/png | 256x240 | 166.3 | tg-6116208243262889961 |
| 10 | ❤️ | image/png | 228x256 | 120.8 | tg-6212808908222765310 |
| 11 | ❤️ | image/png | 251x256 | 178.4 | tg-6215446791236623190 |
| 12 | ❤️ | image/png | 256x189 | 174.2 | tg-6215037442198612558 |
| 13 | ❤️ | image/png | 224x256 | 150.5 | tg-6215316460454027434 |
| 14 | ❤️ | image/png | 204x256 | 159.5 | tg-6215421300605723246 |
| 15 | ❤️ | image/png | 243x256 | 152.4 | tg-6215453693249068532 |
| 16 | ❤️ | image/png | 248x256 | 172.1 | tg-6215407067084106943 |
| 17 | ❤️ | image/png | 253x256 | 155.8 | tg-6115919346582690295 |
| 18 | ❤️ | image/png | 217x256 | 169.0 | tg-6215300040794054563 |
| 19 | ❤️ | image/png | 187x256 | 164.3 | tg-6215249961475381566 |
| 20 | ❤️ | image/png | 209x256 | 169.7 | tg-6327854086897016155 |
| 21 | ❤️ | image/png | 256x219 | 178.1 | tg-6327568282593271398 |
| 22 | ❤️ | image/png | 256x239 | 59.5 | tg-6116064288844030136 |
| 23 | ❤️ | image/png | 256x239 | 65.7 | tg-6116031453819050645 |
| 24 | ❤️ | image/png | 256x239 | 60.7 | tg-6115965624855303988 |
| 25 | ❤️ | image/png | 256x239 | 101.1 | tg-6116267187394058045 |
| 26 | ❤️ | image/png | 256x239 | 44.5 | tg-6115990754708955283 |
| 27 | ❤️ | image/png | 256x239 | 91.0 | tg-6116174484819943430 |
| 28 | ❤️ | image/png | 256x239 | 75.7 | tg-6116166960037240104 |
| 29 | ❤️ | image/png | 256x239 | 44.3 | tg-6116164941402612055 |
| 30 | ❤️ | image/png | 256x239 | 59.3 | tg-6116135035545329192 |
| 31 | ❤️ | image/png | 256x239 | 59.5 | tg-6116302221442292622 |
| 32 | ❤️ | image/png | 256x239 | 48.8 | tg-6116177697455480365 |
| 33 | ❤️ | image/png | 256x239 | 66.5 | tg-6116438689733155732 |
| 34 | ❤️ | image/png | 256x239 | 59.9 | tg-6115946825783451154 |
| 35 | ❤️ | image/png | 256x239 | 45.8 | tg-6116285342220819910 |
| 36 | ❤️ | image/png | 256x239 | 72.6 | tg-6116346962116615475 |


## 26. `方糖小鼠鼠 @zhaxia_cn` — `in_JHCGEC_by_NaiDrawBot.json`

- 標題:`方糖小鼠鼠 @zhaxia_cn`;包 ID:`tg-4209876048168351982`
- 張數:32;mimetype 分佈:image/png ×32
- 大小統計:合計 7,801,927 B(7.44 MB);平均 238.1 KB;最小 147.3 KB;最大 311.1 KB
- 來源 ID:tg- ×32

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 😮 | image/png | 256x256 | 253.7 | tg-6206395551387231074 |
| 2 | 🚫 | image/png | 256x256 | 232.2 | tg-6206062407953947814 |
| 3 | ✅ | image/png | 256x256 | 227.0 | tg-6206107140038336133 |
| 4 | 😤 | image/png | 256x256 | 261.4 | tg-6206085914309958919 |
| 5 | 😄 | image/png | 256x256 | 230.5 | tg-6206232840846188110 |
| 6 | 😭 | image/png | 256x256 | 238.5 | tg-6203735029600755295 |
| 7 | 🚮 | image/png | 256x256 | 311.1 | tg-6206385977905127518 |
| 8 | 🌸 | image/png | 256x256 | 223.9 | tg-6206094564374093500 |
| 9 | ❤️ | image/png | 256x256 | 218.8 | tg-6203787840518627497 |
| 10 | 😮 | image/png | 256x256 | 203.1 | tg-6206178440790417408 |
| 11 | ❤️ | image/png | 256x256 | 225.7 | tg-6206350853662581282 |
| 12 | 👂 | image/png | 256x256 | 248.0 | tg-6203904736643522410 |
| 13 | 🚪 | image/png | 256x256 | 228.9 | tg-6206518194178367162 |
| 14 | 🤗 | image/png | 256x256 | 240.5 | tg-6206420711305650014 |
| 15 | 🐟 | image/png | 256x256 | 243.3 | tg-6206277912232992470 |
| 16 | 🤔 | image/png | 256x256 | 262.9 | tg-6205987924631101194 |
| 17 | 🫠 | image/png | 256x256 | 256.8 | tg-6206304944757153770 |
| 18 | 😏 | image/png | 256x256 | 223.8 | tg-6206052572478839068 |
| 19 | 🚶 | image/png | 256x256 | 259.2 | tg-6206513662987869660 |
| 20 | ❤️ | image/png | 256x256 | 254.2 | tg-6206065577639814637 |
| 21 | 😤 | image/png | 256x256 | 269.6 | tg-6206391436808560444 |
| 22 | 😏 | image/png | 256x256 | 223.4 | tg-6206425246791115374 |
| 23 | 😄 | image/png | 256x256 | 227.6 | tg-6206517086076804107 |
| 24 | 🚮 | image/png | 256x256 | 215.6 | tg-6206316197571468917 |
| 25 | 🚫 | image/png | 256x256 | 260.7 | tg-6206193314262163996 |
| 26 | 😮 | image/png | 256x256 | 240.2 | tg-6206066574072225128 |
| 27 | 🐭 | image/png | 256x256 | 147.3 | tg-6206347142810836545 |
| 28 | 😔 | image/png | 256x256 | 202.1 | tg-6203734630168796809 |
| 29 | 🤔 | image/png | 256x256 | 255.4 | tg-6206465705383042360 |
| 30 | 🤗 | image/png | 256x256 | 222.1 | tg-6205977998961680218 |
| 31 | 🤗 | image/png | 256x256 | 283.1 | tg-6206347756991159194 |
| 32 | 😴 | image/png | 256x256 | 228.1 | tg-6206293863741530324 |


## 27. `lptoy` — `lptoys.json`

- 標題:`lptoy`;包 ID:`tg-290143702477701122`
- 張數:68;mimetype 分佈:image/png ×67;video/webm ×1
- 大小統計:合計 14,695,333 B(14.01 MB);平均 211.0 KB;最小 31.5 KB;最大 444.8 KB
- 來源 ID:tg- ×68

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 😒 | image/png | 256x256 | 218.5 | tg-290143702477701805 |
| 2 | 😐 | image/png | 256x240 | 194.4 | tg-290143702477701806 |
| 3 | 😒 | image/png | 215x256 | 212.1 | tg-290143702477701807 |
| 4 | 😉 | image/png | 256x154 | 162.4 | tg-290143702477701808 |
| 5 | 😡 | image/png | 256x256 | 174.5 | tg-290143702477701809 |
| 6 | 😔 | image/png | 236x256 | 309.5 | tg-290143702477701810 |
| 7 | 😓 | image/png | 255x256 | 174.7 | tg-290143702477701811 |
| 8 | 😓 | image/png | 256x213 | 103.2 | tg-290143702477701812 |
| 9 | 😒 | image/png | 256x208 | 214.8 | tg-290143702477701813 |
| 10 | 😓 | image/png | 256x247 | 231.1 | tg-290143702477701814 |
| 11 | 😥 | image/png | 163x256 | 127.4 | tg-290143702477701815 |
| 12 | 😏 | image/png | 247x256 | 260.2 | tg-290143702477701816 |
| 13 | 😐 | image/png | 256x104 | 31.5 | tg-290143702477701817 |
| 14 | 🖕 | image/png | 256x256 | 250.2 | tg-290143702477701818 |
| 15 | 🔨 | image/png | 256x192 | 240.5 | tg-290143702477701819 |
| 16 | 😟 | image/png | 256x256 | 334.0 | tg-290143702477701820 |
| 17 | 😄 | image/png | 192x256 | 172.6 | tg-290143702477701821 |
| 18 | 😕 | image/png | 251x256 | 154.4 | tg-290143702477701822 |
| 19 | 🤔 | image/png | 256x256 | 81.6 | tg-290143702477701823 |
| 20 | 👍 | image/png | 225x256 | 270.8 | tg-290143702477701824 |
| 21 | 😐 | image/png | 256x186 | 71.7 | tg-290143702477701825 |
| 22 | 😂 | image/png | 256x216 | 200.2 | tg-290143702477701826 |
| 23 | 😟 | image/png | 256x232 | 341.2 | tg-290143702477701827 |
| 24 | 😯 | image/png | 256x256 | 388.1 | tg-290143702477701828 |
| 25 | 😒 | image/png | 256x256 | 109.8 | tg-290143702477701829 |
| 26 | 🤔 | image/png | 232x256 | 199.3 | tg-290143702477701830 |
| 27 | 😒 | image/png | 237x256 | 221.6 | tg-290143702477701831 |
| 28 | 😏 | image/png | 256x256 | 262.3 | tg-290143702477701832 |
| 29 | 🐶 | image/png | 256x256 | 237.5 | tg-290143702477701833 |
| 30 | 🤦‍♂️ | image/png | 256x147 | 119.0 | tg-290143702477701834 |
| 31 | 😠 | image/png | 256x256 | 361.1 | tg-290143702477701835 |
| 32 | 😡 | image/png | 256x245 | 253.6 | tg-290143702477701837 |
| 33 | 😒 | image/png | 256x142 | 149.3 | tg-290143702477701838 |
| 34 | 😡 | image/png | 256x249 | 193.5 | tg-290143702477701839 |
| 35 | 😔 | image/png | 256x256 | 338.1 | tg-5080614031023145262 |
| 36 | 😼 | image/png | 256x256 | 103.0 | tg-5161575036431106437 |
| 37 | 😠 | image/png | 256x256 | 145.6 | tg-5161329892582752512 |
| 38 | 😳 | image/png | 256x200 | 161.5 | tg-5069344865767129994 |
| 39 | 🫡 | image/png | 256x256 | 180.0 | tg-5053511700758660027 |
| 40 | 😒 | image/png | 256x256 | 261.5 | tg-5118504958357930658 |
| 41 | 😐 | image/png | 256x256 | 153.2 | tg-5167966527588139709 |
| 42 | 🤢 | image/png | 256x256 | 298.2 | tg-4942882654702797931 |
| 43 | 😐 | image/png | 256x256 | 52.1 | tg-5186363216841671658 |
| 44 | 😮 | image/png | 256x202 | 78.8 | tg-4940486088721434194 |
| 45 | 🎣 | image/png | 256x256 | 79.6 | tg-4992639953906173135 |
| 46 | 😐 | image/png | 256x256 | 209.2 | tg-4916046410547201048 |
| 47 | 😁 | image/png | 256x256 | 202.5 | tg-5017483195797472601 |
| 48 | 👥 | image/png | 256x150 | 263.2 | tg-5179197665203717559 |
| 49 | 🤨 | image/png | 256x166 | 121.7 | tg-5033328829096002933 |
| 50 | 🤦‍♂️ | image/png | 256x249 | 255.9 | tg-5068894671590130738 |
| 51 | 😐 | image/png | 256x254 | 190.4 | tg-5069249577622701557 |
| 52 | 🤕 | image/png | 256x256 | 270.4 | tg-5089156257118423332 |
| 53 | 😤 | image/png | 235x256 | 295.2 | tg-5143201505641235651 |
| 54 | 🤮 | image/png | 256x256 | 294.6 | tg-5044405992134018674 |
| 55 | 😮‍💨 | image/png | 255x256 | 336.0 | tg-5140988343353346025 |
| 56 | 😱 | image/png | 256x256 | 259.8 | tg-5138683006772315724 |
| 57 | 🙂‍↕️ | image/png | 256x256 | 180.0 | tg-5172664873917614133 |
| 58 | 😒 | image/png | 256x256 | 260.8 | tg-4943120625955768114 |
| 59 | 😨 | image/png | 256x256 | 236.0 | tg-4943216566935226241 |
| 60 | 😬 | image/png | 256x256 | 444.8 | tg-4945407459817686561 |
| 61 | 😳 | image/png | 256x256 | 222.2 | tg-4945194648483137207 |
| 62 | 😭 | image/png | 256x256 | 303.8 | tg-4947226576036038313 |
| 63 | 🫢 | image/png | 256x253 | 155.3 | tg-4951894101680195390 |
| 64 | 😡 | image/png | 256x256 | 177.4 | tg-5032790377636038481 |
| 65 | 😐 | image/png | 256x256 | 209.9 | tg-5035165357111773052 |
| 66 | 🤨 | video/webm | 512x512 | 40.2 | tg-5091792735677975162 |
| 67 | 😒 | image/png | 256x256 | 286.6 | tg-5156998151776765973 |
| 68 | 😂 | image/png | 256x256 | 256.5 | tg-4913558460546682441 |


## 28. `晴の收藏①` — `Qing_Stickers_Collection_1.json`

- 標題:`晴の收藏①`;包 ID:`tg-419111842263072757`
- 張數:102;mimetype 分佈:video/webm ×59;image/png ×43
- 大小統計:合計 15,458,792 B(14.74 MB);平均 148.0 KB;最小 6.3 KB;最大 381.7 KB
- 來源 ID:tg- ×102

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🌟 | image/png | 256x252 | 320.7 | tg-6122898986266271141 |
| 2 | 🙂 | video/webm | 512x512 | 32.3 | tg-6125437505211734861 |
| 3 | 🙂 | video/webm | 512x512 | 54.2 | tg-6217302758274374834 |
| 4 | 🙂 | video/webm | 468x512 | 69.0 | tg-6215362614172589271 |
| 5 | 😀 | image/png | 256x245 | 281.2 | tg-6242043775649061609 |
| 6 | 🌟 | image/png | 256x199 | 144.5 | tg-6124931261711522595 |
| 7 | 🌟 | video/webm | 512x512 | 62.7 | tg-6125190643376463310 |
| 8 | 🌟 | video/webm | 490x512 | 73.8 | tg-6125341057426137656 |
| 9 | 🙂 | video/webm | 512x512 | 77.5 | tg-6124971209202342347 |
| 10 | 😡 | video/webm | 512x478 | 144.0 | tg-6125072042149550526 |
| 11 | 💛 | image/png | 256x256 | 204.2 | tg-6125307453602012693 |
| 12 | 🌟 | video/webm | 512x441 | 73.8 | tg-6125303291778702661 |
| 13 | 🥰 | image/png | 256x256 | 249.8 | tg-6125242981847931613 |
| 14 | 🌟 | video/webm | 290x512 | 140.3 | tg-6125383242594917442 |
| 15 | 🌟 | image/png | 256x213 | 244.5 | tg-6125058890959691819 |
| 16 | 🌟 | image/png | 256x247 | 368.1 | tg-6125420793493986657 |
| 17 | 🌟 | video/webm | 512x512 | 55.5 | tg-6125084978591047377 |
| 18 | 🌟 | video/webm | 512x512 | 120.9 | tg-6190266385822653513 |
| 19 | 🌟 | image/png | 256x200 | 160.0 | tg-6190452512525394723 |
| 20 | 🌟 | image/png | 256x225 | 289.3 | tg-6125417829966551889 |
| 21 | 🌟 | video/webm | 512x512 | 106.5 | tg-6172631683896974906 |
| 22 | 🙂 | video/webm | 512x512 | 67.2 | tg-6125013231162366699 |
| 23 | 🙂 | image/png | 256x256 | 305.6 | tg-6208626404645412057 |
| 24 | 🙂 | video/webm | 512x512 | 40.4 | tg-6251390105521495902 |
| 25 | 🙂 | video/webm | 512x512 | 43.0 | tg-6278188528195082870 |
| 26 | 🙂 | video/webm | 512x512 | 61.5 | tg-6125109562983849420 |
| 27 | 😍 | video/webm | 512x512 | 184.6 | tg-6167761126558801575 |
| 28 | 🙂 | video/webm | 512x400 | 25.0 | tg-6244389081195758280 |
| 29 | 😊 | video/webm | 512x512 | 86.8 | tg-6089064715672101304 |
| 30 | 😊 | video/webm | 512x512 | 21.5 | tg-6089048549415199890 |
| 31 | 🙂 | image/png | 256x256 | 142.8 | tg-6124920077616684721 |
| 32 | 🌟 | video/webm | 512x512 | 234.8 | tg-6124999865224142436 |
| 33 | 🙂 | video/webm | 512x512 | 101.3 | tg-6125077372203965248 |
| 34 | 🎩 | image/png | 256x256 | 134.6 | tg-6125085163274640790 |
| 35 | 🙂 | video/webm | 512x512 | 102.0 | tg-6125427356204014962 |
| 36 | 🙂 | image/png | 256x256 | 280.2 | tg-6125197163136817681 |
| 37 | ⭐ | video/webm | 512x512 | 181.1 | tg-6125150627166166673 |
| 38 | ⭐ | video/webm | 465x512 | 96.4 | tg-6125318169545416647 |
| 39 | 🌚 | video/webm | 512x512 | 101.0 | tg-6149852680597544502 |
| 40 | 🌟 | image/png | 256x256 | 270.4 | tg-6127152425523485974 |
| 41 | 🙂 | video/webm | 512x512 | 133.2 | tg-6127428402942056828 |
| 42 | 🙂 | video/webm | 512x512 | 37.4 | tg-6129609859781368900 |
| 43 | 🌟 | video/webm | 512x512 | 49.7 | tg-6129527018452163043 |
| 44 | 🌟 | video/webm | 512x491 | 6.3 | tg-6129503954477789225 |
| 45 | 🙂 | image/png | 256x256 | 247.8 | tg-6147847841403380017 |
| 46 | 😡 | video/webm | 512x512 | 223.4 | tg-6129491945749225457 |
| 47 | 😍 | image/png | 256x256 | 253.0 | tg-6082635106680316685 |
| 48 | 🌟 | image/png | 256x251 | 317.3 | tg-6131880394242399276 |
| 49 | ⭐ | image/png | 226x256 | 245.5 | tg-6140819251977526084 |
| 50 | 🙂 | video/webm | 512x230 | 18.2 | tg-6136413985626398385 |
| 51 | 😯 | image/png | 256x256 | 285.8 | tg-6140662318167498317 |
| 52 | 🙂 | image/png | 256x256 | 137.0 | tg-6147700777428197253 |
| 53 | 🌟 | video/webm | 512x512 | 160.0 | tg-6147727298851249371 |
| 54 | 🌟 | image/png | 256x177 | 223.1 | tg-6150021678970706977 |
| 55 | 🌟 | video/webm | 512x500 | 47.8 | tg-6150162231775470189 |
| 56 | ⭐ | video/webm | 451x512 | 94.5 | tg-6152083568215464444 |
| 57 | 🙂 | video/webm | 512x400 | 11.8 | tg-6190563563199798143 |
| 58 | 🌟 | video/webm | 512x512 | 31.9 | tg-6190402411731886157 |
| 59 | 🌟 | image/png | 201x256 | 151.7 | tg-6190362584500148320 |
| 60 | 🍟 | image/png | 256x256 | 244.1 | tg-6197020539723193535 |
| 61 | 🌟 | video/webm | 512x476 | 8.7 | tg-6199236785797602940 |
| 62 | 🙂 | video/webm | 512x512 | 94.7 | tg-6206029267986291402 |
| 63 | 🤪 | video/webm | 512x512 | 71.9 | tg-6206414393408757371 |
| 64 | 🙂 | image/png | 256x256 | 290.1 | tg-6208766824306187846 |
| 65 | 🌟 | image/png | 256x256 | 193.6 | tg-6210911417441197153 |
| 66 | 🌟 | image/png | 256x249 | 180.9 | tg-6215016177815526868 |
| 67 | 🌟 | video/webm | 512x496 | 10.8 | tg-6212989657626450107 |
| 68 | 🐱 | image/png | 256x256 | 194.4 | tg-6213006081581391137 |
| 69 | 🌟 | video/webm | 512x512 | 175.7 | tg-6215446228595908375 |
| 70 | 🙂 | image/png | 256x256 | 381.7 | tg-6215414475902689838 |
| 71 | 🙂 | image/png | 256x256 | 219.6 | tg-6217498849301240890 |
| 72 | 🙂 | image/png | 256x256 | 236.7 | tg-6217304102599141207 |
| 73 | 🏳️ | video/webm | 310x512 | 57.6 | tg-6230880829229244900 |
| 74 | 🌟 | video/webm | 512x512 | 51.6 | tg-6237664596929289076 |
| 75 | 🌟 | video/webm | 512x512 | 200.1 | tg-6239824278284410115 |
| 76 | 🐶 | video/webm | 512x288 | 14.6 | tg-6239804865032232212 |
| 77 | 😵‍💫 | video/webm | 512x512 | 107.9 | tg-6238040982093308014 |
| 78 | 😧 | video/webm | 288x512 | 153.8 | tg-6237617700181384516 |
| 79 | 😅 | video/webm | 512x302 | 52.0 | tg-6237782966227967770 |
| 80 | 🌟 | image/png | 256x256 | 366.5 | tg-6244448287319923933 |
| 81 | 🙂 | video/webm | 512x512 | 63.5 | tg-6251044764381095830 |
| 82 | 🙂 | image/png | 256x256 | 254.2 | tg-6282738058202717672 |
| 83 | 🙂 | video/webm | 512x512 | 142.3 | tg-6287283623955537498 |
| 84 | 🤤 | image/png | 188x256 | 227.0 | tg-6305270083702759245 |
| 85 | 🌟 | video/webm | 400x512 | 70.1 | tg-6307693480344821755 |
| 86 | 🙂 | video/webm | 512x512 | 78.7 | tg-6318655783072439669 |
| 87 | 🥱 | video/webm | 512x512 | 107.8 | tg-6332522093577510799 |
| 88 | 😔 | image/png | 256x256 | 140.0 | tg-6336904381853604946 |
| 89 | 🥵 | video/webm | 339x512 | 89.0 | tg-6082542163588030136 |
| 90 | 🌟 | video/webm | 512x512 | 19.2 | tg-6086799202027839595 |
| 91 | ☝️ | image/png | 256x256 | 126.4 | tg-6095892261973795185 |
| 92 | ☺️ | video/webm | 349x512 | 90.6 | tg-6100186108283331859 |
| 93 | 😊 | video/webm | 512x512 | 253.5 | tg-6107076850733817723 |
| 94 | 🙂 | image/png | 256x256 | 167.0 | tg-6141213693184058079 |
| 95 | 🙂 | image/png | 256x256 | 200.8 | tg-6149785545963740782 |
| 96 | 🙂 | video/webm | 512x512 | 94.5 | tg-6188017927493525106 |
| 97 | 🫥 | image/png | 256x256 | 181.2 | tg-6190216594266791216 |
| 98 | 🙂 | image/png | 256x256 | 209.1 | tg-6205998975581954752 |
| 99 | 🌟 | image/png | 256x159 | 220.1 | tg-6294315198383660825 |
| 100 | 🙂 | image/png | 256x256 | 96.1 | tg-6309700776260280823 |
| 101 | 🙂 | image/png | 256x256 | 251.5 | tg-6312058867924607077 |
| 102 | 🙂 | image/png | 256x256 | 278.0 | tg-6312104072455398521 |


## 29. `SkipM44贴纸2` — `SkipM44_2_by_fStikBot.json`

- 標題:`SkipM44贴纸2`;包 ID:`tg-5777884559722938363`
- 張數:98;mimetype 分佈:image/png ×91;video/webm ×7
- 大小統計:合計 20,044,041 B(19.12 MB);平均 199.7 KB;最小 30.1 KB;最大 377.9 KB
- 來源 ID:tg- ×98

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🥵 | image/png | 250x256 | 342.5 | tg-6169936845321802697 |
| 2 | 😆 | image/png | 256x238 | 232.0 | tg-6125401749608994018 |
| 3 | 😈 | image/png | 256x168 | 166.1 | tg-6325382526491693869 |
| 4 | 😡 | image/png | 231x256 | 352.1 | tg-6237618739563467882 |
| 5 | 🥵 | image/png | 256x248 | 316.9 | tg-6303284885394035224 |
| 6 | 😈 | image/png | 239x256 | 375.4 | tg-6192661568824547089 |
| 7 | 😯 | image/png | 256x256 | 291.6 | tg-6327597243557744380 |
| 8 | 😠 | image/png | 256x236 | 318.5 | tg-6075595955929879174 |
| 9 | 🥰 | video/webm | 512x512 | 30.1 | tg-6192797298381034187 |
| 10 | 😡 | image/png | 256x249 | 268.7 | tg-6291748242459727681 |
| 11 | 😨 | image/png | 256x256 | 265.4 | tg-6228765231418446282 |
| 12 | 😨 | image/png | 256x175 | 176.2 | tg-6249203765304364697 |
| 13 | 😨 | image/png | 256x256 | 282.8 | tg-6244537682769219171 |
| 14 | 😎 | image/png | 256x175 | 114.8 | tg-6267027647654531853 |
| 15 | 👉 | image/png | 256x189 | 246.5 | tg-6228837567257644997 |
| 16 | 😠 | image/png | 256x256 | 276.7 | tg-6248926611064754796 |
| 17 | 😏 | image/png | 256x213 | 171.6 | tg-6325779527498731630 |
| 18 | 😓 | image/png | 211x256 | 288.9 | tg-6253723020087529653 |
| 19 | 😡 | image/png | 256x251 | 177.9 | tg-6197144058687657573 |
| 20 | 🤥 | image/png | 253x256 | 220.1 | tg-6053072460234888633 |
| 21 | 😮 | image/png | 204x256 | 219.8 | tg-6068944786755164329 |
| 22 | 😩 | image/png | 256x249 | 204.7 | tg-6195194315333966393 |
| 23 | 😫 | image/png | 256x152 | 146.0 | tg-6116263837319567086 |
| 24 | 😫 | image/png | 256x204 | 176.8 | tg-6097907250175678528 |
| 25 | 😦 | image/png | 197x256 | 204.8 | tg-6062161749199559778 |
| 26 | 😮 | image/png | 241x256 | 130.0 | tg-6246959292704887993 |
| 27 | 🙄 | image/png | 219x256 | 174.8 | tg-6093749034638384975 |
| 28 | 😡 | image/png | 256x241 | 293.0 | tg-6312058197909708334 |
| 29 | 👐 | image/png | 256x208 | 245.9 | tg-6339226709325259194 |
| 30 | 🤨 | image/png | 195x256 | 214.2 | tg-6253361418200946502 |
| 31 | 🤯 | image/png | 256x256 | 353.6 | tg-6132093038073222299 |
| 32 | 😭 | image/png | 256x188 | 229.5 | tg-6129519596748674285 |
| 33 | 😭 | image/png | 196x256 | 184.4 | tg-6080056859287361666 |
| 34 | 😨 | image/png | 256x251 | 197.3 | tg-6116029134536710077 |
| 35 | 😓 | image/png | 242x256 | 181.6 | tg-6323425902600393413 |
| 36 | 😕 | image/png | 256x183 | 151.7 | tg-6156899201511856316 |
| 37 | 🤓 | image/png | 212x256 | 271.0 | tg-6217279277688166504 |
| 38 | 🔪 | image/png | 245x256 | 176.2 | tg-6217629248803313748 |
| 39 | 😈 | image/png | 256x148 | 207.9 | tg-6327753395683728870 |
| 40 | 😦 | image/png | 256x117 | 41.5 | tg-6161103914365099895 |
| 41 | 😦 | image/png | 256x117 | 40.2 | tg-6160947822368661230 |
| 42 | 😀 | image/png | 256x241 | 269.7 | tg-6235696234892369955 |
| 43 | 🌈 | image/png | 256x194 | 253.4 | tg-6235537011864772440 |
| 44 | 😈 | image/png | 243x256 | 164.7 | tg-6235657451337687200 |
| 45 | 😐 | image/png | 256x143 | 94.8 | tg-6242094688191389459 |
| 46 | 🙂 | image/png | 256x168 | 249.9 | tg-6242064584765612223 |
| 47 | 😨 | image/png | 256x221 | 255.8 | tg-6242088851330835312 |
| 48 | 😈 | image/png | 256x215 | 308.6 | tg-6120625621421792056 |
| 49 | 🤨 | video/webm | 454x512 | 31.2 | tg-6271662067690770588 |
| 50 | 😡 | image/png | 239x256 | 199.2 | tg-6075568317815329266 |
| 51 | 😵 | image/png | 256x256 | 201.0 | tg-6219796472121005335 |
| 52 | ⚡ | image/png | 193x256 | 255.2 | tg-6228690009361228878 |
| 53 | 😆 | video/webm | 473x512 | 62.7 | tg-6249053750686650413 |
| 54 | 🧐 | video/webm | 512x512 | 101.3 | tg-6057563479903047957 |
| 55 | 😡 | image/png | 256x212 | 149.1 | tg-6309624128273912004 |
| 56 | 😈 | image/png | 256x256 | 107.8 | tg-6084512131942716836 |
| 57 | 😮 | image/png | 256x249 | 147.7 | tg-6210831625538770957 |
| 58 | 🌟 | video/webm | 512x480 | 70.1 | tg-6222136597937131572 |
| 59 | 👀 | image/png | 204x256 | 299.4 | tg-6307404068268545375 |
| 60 | 🤯 | image/png | 256x234 | 208.3 | tg-6127581192108643505 |
| 61 | 😒 | image/png | 256x223 | 202.5 | tg-6134342527194501236 |
| 62 | 😓 | video/webm | 512x410 | 148.7 | tg-6309887688942032325 |
| 63 | 😄 | image/png | 256x191 | 245.1 | tg-6280663971250837682 |
| 64 | 🤓 | image/png | 256x207 | 253.9 | tg-6302924743796333173 |
| 65 | 😒 | image/png | 256x256 | 303.2 | tg-6213144327988712388 |
| 66 | 🤓 | image/png | 256x219 | 193.2 | tg-6172513074080127548 |
| 67 | 😬 | video/webm | 509x512 | 70.5 | tg-6174985351744984828 |
| 68 | 😇 | image/png | 165x256 | 266.5 | tg-6336644424663045811 |
| 69 | 🤑 | image/png | 256x173 | 222.9 | tg-6337098784958321768 |
| 70 | 😎 | image/png | 181x256 | 144.8 | tg-6334503958991607894 |
| 71 | 😯 | image/png | 252x256 | 252.9 | tg-6087153695743546990 |
| 72 | 😒 | image/png | 223x256 | 177.9 | tg-6120937195529311953 |
| 73 | 🤠 | image/png | 256x164 | 113.4 | tg-6253689076960991788 |
| 74 | 👊 | image/png | 247x256 | 190.6 | tg-6253381179345477051 |
| 75 | 😫 | image/png | 256x144 | 171.1 | tg-6253695231649129122 |
| 76 | 😡 | image/png | 256x249 | 205.5 | tg-6271359856611957096 |
| 77 | 🖐 | image/png | 254x256 | 377.9 | tg-6271645093980018870 |
| 78 | 🤣 | image/png | 109x256 | 106.1 | tg-6264523647361226500 |
| 79 | 😁 | image/png | 154x256 | 151.7 | tg-6053159914358972438 |
| 80 | 😊 | image/png | 256x217 | 309.9 | tg-6077633539954715362 |
| 81 | 😏 | image/png | 256x143 | 218.6 | tg-6140999812402650431 |
| 82 | 😙 | image/png | 256x198 | 227.9 | tg-6224174229206605408 |
| 83 | 😯 | image/png | 253x256 | 253.5 | tg-6201561054594474073 |
| 84 | 🫨 | image/png | 256x171 | 131.0 | tg-6199580924347162575 |
| 85 | 😬 | image/png | 256x256 | 150.9 | tg-6235460157719977383 |
| 86 | 🔫 | image/png | 218x256 | 165.2 | tg-6271760529816033611 |
| 87 | 💫 | image/png | 256x228 | 128.0 | tg-6098280585912917783 |
| 88 | 👿 | image/png | 256x234 | 160.8 | tg-6258145921574381167 |
| 89 | 😈 | image/png | 255x256 | 142.8 | tg-6242475540121391606 |
| 90 | 👿 | image/png | 256x252 | 199.9 | tg-6087003844334589046 |
| 91 | 😈 | image/png | 256x115 | 116.6 | tg-6084497060902476193 |
| 92 | 😵 | image/png | 256x187 | 248.9 | tg-6177011506861842302 |
| 93 | 😃 | image/png | 256x178 | 172.3 | tg-6196979733238916509 |
| 94 | 👏 | image/png | 185x256 | 147.4 | tg-6242448344388477775 |
| 95 | 😄 | image/png | 189x256 | 213.8 | tg-6300917181592904596 |
| 96 | 😐 | image/png | 252x256 | 145.2 | tg-6300650180655980411 |
| 97 | 😐 | image/png | 171x256 | 49.3 | tg-6314176183722320648 |
| 98 | 😡 | image/png | 192x256 | 204.1 | tg-6300906173591724584 |


## 30. `TEmPTaTi♂N :: @fStikBot` — `a01fe077_by_fStikBot.json`

- 標題:`TEmPTaTi♂N :: @fStikBot`;包 ID:`tg-3758463900048162803`
- 張數:76;mimetype 分佈:image/png ×76
- 大小統計:合計 15,821,468 B(15.09 MB);平均 203.3 KB;最小 64.5 KB;最大 376.9 KB
- 來源 ID:tg- ×76

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 😱 | image/png | 256x144 | 126.7 | tg-5102760587503338472 |
| 2 | 😅 | image/png | 256x245 | 312.4 | tg-5100743267134211174 |
| 3 | 👇 | image/png | 256x223 | 95.4 | tg-5102672978760435033 |
| 4 | 🤔 | image/png | 256x233 | 161.8 | tg-5100533419327095797 |
| 5 | 🤔 | image/png | 252x256 | 199.3 | tg-5100442550704014492 |
| 6 | 🤗 | image/png | 256x221 | 301.2 | tg-5100793088754844821 |
| 7 | 🥵 | image/png | 256x192 | 188.1 | tg-5100710522303546356 |
| 8 | 😅 | image/png | 219x256 | 133.5 | tg-5100681690188088179 |
| 9 | 🈲️ | image/png | 256x230 | 345.9 | tg-5103023641365316668 |
| 10 | 🏃 | image/png | 256x256 | 249.5 | tg-5102679335312033053 |
| 11 | 😅 | image/png | 256x251 | 236.6 | tg-5102637936122266653 |
| 12 | 👏 | image/png | 256x197 | 159.4 | tg-5102896922650215803 |
| 13 | 😈 | image/png | 249x256 | 217.5 | tg-5102900165350523865 |
| 14 | 🗣️ | image/png | 256x256 | 155.3 | tg-5103042955833247051 |
| 15 | 😡 | image/png | 256x256 | 266.3 | tg-5102683217962468663 |
| 16 | 😋 | image/png | 256x232 | 198.4 | tg-5102865925871240321 |
| 17 | 😅 | image/png | 241x256 | 159.8 | tg-5100756890770474187 |
| 18 | 😨 | image/png | 256x209 | 194.7 | tg-5102880004774036630 |
| 19 | 🛌 | image/png | 256x256 | 289.7 | tg-5102719433126708617 |
| 20 | ❓ | image/png | 210x256 | 134.5 | tg-5100599634837898112 |
| 21 | 😏 | image/png | 212x256 | 164.5 | tg-5100386595870082400 |
| 22 | 😴 | image/png | 253x256 | 190.4 | tg-5102601269986460983 |
| 23 | 😅 | image/png | 256x253 | 215.6 | tg-5102862541437010996 |
| 24 | 👎 | image/png | 256x213 | 185.2 | tg-5100381240045863948 |
| 25 | 😢 | image/png | 256x173 | 194.9 | tg-5102776427342726219 |
| 26 | 🖕 | image/png | 256x224 | 230.9 | tg-5102654725149426385 |
| 27 | 🤧 | image/png | 256x241 | 236.3 | tg-5103094516915634973 |
| 28 | 🚲 | image/png | 192x256 | 373.0 | tg-5102720652897420721 |
| 29 | 😈 | image/png | 256x167 | 259.4 | tg-5100826851492759351 |
| 30 | 😅 | image/png | 256x195 | 290.7 | tg-5102718213355996977 |
| 31 | 🫣 | image/png | 256x256 | 154.6 | tg-5100660309840889317 |
| 32 | 🗣️ | image/png | 256x241 | 188.5 | tg-5102811229462725428 |
| 33 | 😰 | image/png | 256x241 | 189.7 | tg-5102649665677951952 |
| 34 | 😡 | image/png | 256x256 | 115.2 | tg-5102702111523603822 |
| 35 | 😨 | image/png | 256x254 | 278.0 | tg-5102687959606363183 |
| 36 | 👆 | image/png | 236x256 | 181.1 | tg-5102868511441552257 |
| 37 | 😓 | image/png | 180x256 | 167.3 | tg-5102671707450115099 |
| 38 | 👍 | image/png | 256x170 | 255.8 | tg-5102687431325385617 |
| 39 | ⏰ | image/png | 256x164 | 172.6 | tg-5102676504928584829 |
| 40 | 😈 | image/png | 185x256 | 163.9 | tg-5100436490505159704 |
| 41 | 🤬 | image/png | 256x256 | 138.4 | tg-5100384315242447931 |
| 42 | 😡 | image/png | 256x231 | 149.2 | tg-5103043496999126144 |
| 43 | 🖕 | image/png | 256x256 | 155.5 | tg-5102987731143755564 |
| 44 | 🖕 | image/png | 256x256 | 103.6 | tg-5103073643374576823 |
| 45 | 😡 | image/png | 256x215 | 245.6 | tg-5102901273452085985 |
| 46 | 🦸‍♂️ | image/png | 167x256 | 257.7 | tg-5103012190982505501 |
| 47 | 😅 | image/png | 256x230 | 115.9 | tg-5103119260222227291 |
| 48 | 😡 | image/png | 256x243 | 136.5 | tg-5103077014923903916 |
| 49 | 😡 | image/png | 256x225 | 174.3 | tg-5100515891565561008 |
| 50 | 😨 | image/png | 256x256 | 200.6 | tg-5103013741465699391 |
| 51 | 👎 | image/png | 256x177 | 215.5 | tg-5103093984339690716 |
| 52 | 😡 | image/png | 256x214 | 105.5 | tg-5102833357134234642 |
| 53 | 🏌️ | image/png | 256x245 | 149.0 | tg-5100763324631483327 |
| 54 | 🤙 | image/png | 256x256 | 329.7 | tg-5102667854864450654 |
| 55 | ❓ | image/png | 256x108 | 137.2 | tg-5102857855627691188 |
| 56 | 😃 | image/png | 256x75 | 113.0 | tg-5103094985067070800 |
| 57 | 🐻 | image/png | 256x256 | 200.4 | tg-5102809240892867670 |
| 58 | ✨ | image/png | 256x256 | 212.6 | tg-5102650936988271475 |
| 59 | ✨ | image/png | 254x256 | 297.8 | tg-5100600532486064375 |
| 60 | 🎧 | image/png | 256x191 | 159.6 | tg-5102710495299765268 |
| 61 | 🌟 | image/png | 247x256 | 202.5 | tg-5102594604197217103 |
| 62 | 🌟 | image/png | 192x256 | 197.8 | tg-5102655524013343770 |
| 63 | 🌟 | image/png | 256x256 | 233.5 | tg-5102689935291319682 |
| 64 | 🌟 | image/png | 256x256 | 254.5 | tg-5102973321528476944 |
| 65 | 🌟 | image/png | 256x256 | 157.6 | tg-5102708863212192632 |
| 66 | 🖼️ | image/png | 252x256 | 312.3 | tg-5102601128252539873 |
| 67 | 🖼️ | image/png | 256x227 | 99.9 | tg-5102739933005612144 |
| 68 | 🌟 | image/png | 256x256 | 376.9 | tg-5104857652530251007 |
| 69 | 🖼️ | image/png | 256x96 | 64.5 | tg-4954402113472955561 |
| 70 | 🌟 | image/png | 256x255 | 280.6 | tg-5098340220047197401 |
| 71 | 🌟 | image/png | 223x256 | 208.2 | tg-5098080211317032267 |
| 72 | 🌟 | image/png | 256x221 | 188.0 | tg-5098359190917743634 |
| 73 | 🌟 | image/png | 256x256 | 268.4 | tg-5059979818427221264 |
| 74 | 🌟 | image/png | 256x250 | 196.5 | tg-5060266249796191333 |
| 75 | 🌟 | image/png | 256x256 | 219.3 | tg-5062134161137992666 |
| 76 | 🌟 | image/png | 256x256 | 259.1 | tg-5080618218616259546 |


## 31. `小火切 @zhaxia_cn` — `in_DDBIDC_by_NaiDrawBot.json`

- 標題:`小火切 @zhaxia_cn`;包 ID:`tg-4209876048168353416`
- 張數:90;mimetype 分佈:image/png ×89;video/webm ×1
- 大小統計:合計 24,876,260 B(23.72 MB);平均 269.9 KB;最小 66.1 KB;最大 486.2 KB
- 來源 ID:tg- ×90

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | ❤️ | image/png | 256x256 | 269.2 | tg-6336951725278104721 |
| 2 | 🔥 | image/png | 256x256 | 323.9 | tg-6336603716963012480 |
| 3 | 👧 | image/png | 256x256 | 252.3 | tg-6334541119048651525 |
| 4 | 🛑 | image/png | 256x256 | 254.9 | tg-6336858477243141829 |
| 5 | 👍 | image/png | 256x256 | 255.7 | tg-6337005137491398061 |
| 6 | 👊 | image/png | 256x256 | 218.4 | tg-6336879535467794579 |
| 7 | 👊 | image/png | 256x256 | 231.6 | tg-6334315732049858906 |
| 8 | 😱 | image/png | 256x256 | 244.1 | tg-6334865633892634065 |
| 9 | 👩 | image/png | 256x256 | 271.1 | tg-6334442605383781878 |
| 10 | 😔 | image/png | 256x256 | 289.9 | tg-6334788015243660441 |
| 11 | 🔓 | image/png | 256x256 | 243.3 | tg-6336978959665729189 |
| 12 | 🤬 | image/png | 256x256 | 261.7 | tg-6334549824947360292 |
| 13 | 👶 | image/png | 256x256 | 239.9 | tg-6334315079214829264 |
| 14 | 🔥 | image/png | 256x256 | 288.2 | tg-6336895465501495251 |
| 15 | 🚫 | image/png | 256x256 | 161.1 | tg-6334705852519289385 |
| 16 | 😰 | image/png | 256x256 | 267.4 | tg-6336661187920399449 |
| 17 | ❤️ | image/png | 256x256 | 232.8 | tg-6318902683562414101 |
| 18 | 👩 | image/png | 256x256 | 264.9 | tg-6318611420355236227 |
| 19 | ❤️ | image/png | 256x256 | 266.7 | tg-6319054716814758693 |
| 20 | 🏟️ | image/png | 256x256 | 298.2 | tg-6321194460931691955 |
| 21 | ❤️ | image/png | 256x256 | 258.7 | tg-6318824875934880161 |
| 22 | 👉 | image/png | 256x256 | 229.4 | tg-6318990962320216525 |
| 23 | 🌡️ | image/png | 256x256 | 239.4 | tg-6318945036234920910 |
| 24 | 🧙 | image/png | 256x256 | 279.1 | tg-6318736485507927985 |
| 25 | 👌 | image/png | 256x256 | 197.0 | tg-6318720297776190887 |
| 26 | ❤️ | image/png | 256x256 | 267.2 | tg-6318562075475972272 |
| 27 | 👤 | image/png | 256x256 | 177.5 | tg-6318551041704988583 |
| 28 | ❤️ | image/png | 256x256 | 252.8 | tg-6318729832603587972 |
| 29 | ❤️ | image/png | 256x256 | 245.9 | tg-6320954655727686480 |
| 30 | ❤️ | image/png | 256x256 | 222.0 | tg-6318905994982199785 |
| 31 | 😱 | image/png | 256x256 | 253.0 | tg-6318978476850287671 |
| 32 | ❤️ | image/png | 256x256 | 289.5 | tg-6318579654777113963 |
| 33 | 🚫 | image/png | 256x256 | 270.4 | tg-6082215359526474479 |
| 34 | 👫 | image/png | 256x256 | 258.1 | tg-6082580904193036888 |
| 35 | ☄️ | image/png | 256x256 | 398.5 | tg-6082143414529299964 |
| 36 | 🚫 | image/png | 256x256 | 119.4 | tg-6089231978878473247 |
| 37 | 🔴 | image/png | 256x256 | 218.8 | tg-6088950491016860807 |
| 38 | 🍺 | image/png | 256x256 | 272.4 | tg-6086966533953688989 |
| 39 | ❤️ | image/png | 256x256 | 257.4 | tg-6134014245664199107 |
| 40 | 🍵 | image/png | 256x256 | 150.8 | tg-6136285725018045301 |
| 41 | 🤔 | image/png | 256x256 | 241.2 | tg-6134224926694970184 |
| 42 | 💰 | image/png | 256x256 | 256.5 | tg-6134341118445227825 |
| 43 | 🤔 | image/png | 256x256 | 255.5 | tg-6172375081075873358 |
| 44 | ❤️ | image/png | 256x256 | 224.9 | tg-6174524527523927203 |
| 45 | 📝 | image/png | 256x256 | 280.7 | tg-6174715941331408528 |
| 46 | 🥚 | image/png | 256x256 | 229.3 | tg-6172534042110466499 |
| 47 | 🚫 | image/png | 256x256 | 224.0 | tg-6174714867589584861 |
| 48 | 👷 | image/png | 256x256 | 318.8 | tg-6174664934299802267 |
| 49 | ❤️ | image/png | 256x256 | 256.1 | tg-6174510302592244244 |
| 50 | 🎮 | image/png | 256x256 | 358.9 | tg-6174893014243087599 |
| 51 | 😮 | image/png | 256x256 | 255.0 | tg-6174450675561272967 |
| 52 | 😭 | image/png | 256x256 | 311.0 | tg-6174446797205804454 |
| 53 | 🤰 | image/png | 256x256 | 321.5 | tg-6174473808255129123 |
| 54 | 👧 | image/png | 256x256 | 258.0 | tg-6172221123678181349 |
| 55 | 🦊 | image/png | 256x256 | 463.8 | tg-6174826635523528598 |
| 56 | 👂 | image/png | 256x256 | 245.3 | tg-6172691508496437901 |
| 57 | 🐉 | image/png | 256x256 | 290.8 | tg-6172571369671235086 |
| 58 | 🏆 | image/png | 256x256 | 208.4 | tg-6174871535111641291 |
| 59 | 🚶 | image/png | 256x256 | 256.2 | tg-6242286136358606576 |
| 60 | 👊 | image/png | 256x256 | 296.8 | tg-6242325723072174781 |
| 61 | 👊 | image/png | 256x256 | 344.6 | tg-6242197166111069614 |
| 62 | 🤪 | image/png | 256x256 | 294.4 | tg-6242092197110355679 |
| 63 | 🤚 | image/png | 256x256 | 297.6 | tg-6242320435967432564 |
| 64 | ❤️ | image/png | 256x256 | 285.1 | tg-6242098635266332254 |
| 65 | 👀 | image/png | 256x256 | 304.8 | tg-6242228729825728536 |
| 66 | 🤔 | image/png | 256x256 | 282.8 | tg-6242123825249523635 |
| 67 | ❤️ | image/png | 256x256 | 286.7 | tg-6242064528931034367 |
| 68 | 🌞 | image/png | 256x256 | 366.4 | tg-6242349976752495192 |
| 69 | ❤️ | image/png | 256x256 | 419.2 | tg-6242494510991939098 |
| 70 | 😤 | image/png | 256x256 | 341.7 | tg-6242111193750704830 |
| 71 | 🤔 | image/png | 256x256 | 238.5 | tg-6242004730101375559 |
| 72 | 👌 | image/png | 256x256 | 211.7 | tg-6239986327400486937 |
| 73 | ❤️ | image/png | 256x256 | 230.7 | tg-6242041722654693498 |
| 74 | 👧 | image/png | 256x256 | 258.1 | tg-6242119371368438787 |
| 75 | 😵 | image/png | 256x256 | 486.2 | tg-6091536744228854199 |
| 76 | 🎨 | image/png | 256x256 | 456.5 | tg-6091194821882419069 |
| 77 | 😊 | image/png | 256x256 | 307.8 | tg-6091205494876149519 |
| 78 | 😊 | image/png | 256x256 | 220.3 | tg-6091379814713792924 |
| 79 | 🧙 | image/png | 256x256 | 241.6 | tg-6089234083412448744 |
| 80 | ❤️ | image/png | 256x256 | 309.3 | tg-6089035316620958034 |
| 81 | ❤️ | image/png | 256x256 | 307.2 | tg-6091455341713693000 |
| 82 | 🤔 | image/png | 256x256 | 277.1 | tg-6091416425015022921 |
| 83 | 😤 | image/png | 256x256 | 214.2 | tg-6091666061399171311 |
| 84 | ❤️ | image/png | 256x256 | 161.0 | tg-6091152172857169014 |
| 85 | 🔪 | image/png | 256x256 | 250.5 | tg-6091430886169910381 |
| 86 | 🚶 | image/png | 256x256 | 312.8 | tg-6091551858218769055 |
| 87 | 💰 | image/png | 256x256 | 281.4 | tg-6088987775627958424 |
| 88 | 🔨 | video/webm | 512x512 | 66.1 | tg-6091337831408475318 |
| 89 | 📌 | image/png | 256x256 | 272.4 | tg-6091679758049876559 |
| 90 | ❤️ | image/png | 256x256 | 421.2 | tg-6091428906189985995 |


## 32. `嘿嘿～吃干抹净～♡♡ :: @fStikBot` — `fa1_qing2_san4_hua2_by_fStikBot.json`

- 標題:`嘿嘿～吃干抹净～♡♡ :: @fStikBot`;包 ID:`tg-4164737221783453694`
- 張數:119;mimetype 分佈:image/png ×102;video/webm ×17
- 大小統計:合計 27,864,604 B(26.57 MB);平均 228.7 KB;最小 15.5 KB;最大 542.4 KB
- 來源 ID:tg- ×119

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🌟 | video/webm | 512x512 | 216.2 | tg-6093447424854989088 |
| 2 | 🍑 | image/png | 256x256 | 237.3 | tg-6093810517095225955 |
| 3 | 🫥 | image/png | 256x256 | 265.4 | tg-6091414221696800967 |
| 4 | 🫥 | image/png | 256x256 | 220.1 | tg-6091499743085598512 |
| 5 | 🐦 | image/png | 256x256 | 231.9 | tg-6091600807961040651 |
| 6 | 🥺 | image/png | 256x256 | 215.2 | tg-6093616947214163346 |
| 7 | ❤ | image/png | 256x224 | 276.9 | tg-6091136607895689066 |
| 8 | ⭐ | image/png | 256x200 | 261.5 | tg-6091462686107769377 |
| 9 | 😍 | image/png | 256x192 | 162.4 | tg-6091338230840433954 |
| 10 | ❤️ | image/png | 256x203 | 93.9 | tg-6093815086940429243 |
| 11 | ✋ | image/png | 256x256 | 137.6 | tg-6091512670937161054 |
| 12 | ❤ | image/png | 256x256 | 278.8 | tg-6091606533152447114 |
| 13 | 😊 | image/png | 256x246 | 203.5 | tg-6093495756121970690 |
| 14 | 😔 | image/png | 256x256 | 296.5 | tg-6091498987171355355 |
| 15 | 😟 | image/png | 233x256 | 206.1 | tg-6091214123465447809 |
| 16 | 🥲 | image/png | 256x246 | 367.2 | tg-6091570481196964834 |
| 17 | 🔥 | image/png | 256x256 | 173.5 | tg-6091398785584339387 |
| 18 | 👍 | image/png | 256x256 | 230.8 | tg-6091638715342395627 |
| 19 | 🌟 | image/png | 170x256 | 145.3 | tg-6093889991170070928 |
| 20 | 🌟 | image/png | 256x248 | 244.0 | tg-6091634772562417945 |
| 21 | 🌟 | image/png | 256x189 | 305.6 | tg-6091224439976892999 |
| 22 | ✨ | image/png | 256x177 | 228.5 | tg-6091242478839536641 |
| 23 | ⭐ | video/webm | 512x512 | 39.8 | tg-6093687938728598580 |
| 24 | 🌟 | image/png | 175x256 | 68.2 | tg-6093543975719803237 |
| 25 | 🥵 | image/png | 256x256 | 319.5 | tg-6091251163263409458 |
| 26 | 🥵 | image/png | 256x256 | 318.5 | tg-6091136161219090600 |
| 27 | 🙃 | image/png | 230x256 | 320.8 | tg-6093818832151909767 |
| 28 | ❤ | image/png | 256x256 | 332.4 | tg-6093604702262401313 |
| 29 | ❤ | video/webm | 512x288 | 90.4 | tg-6091302329208806078 |
| 30 | 😍 | image/png | 256x183 | 270.8 | tg-6091436259173997245 |
| 31 | 🌟 | image/png | 256x226 | 289.6 | tg-6093388210140878678 |
| 32 | 🥵 | image/png | 256x256 | 311.3 | tg-6093415315679484550 |
| 33 | ✨ | image/png | 170x256 | 257.3 | tg-6091451373163912193 |
| 34 | 😍 | image/png | 256x256 | 297.2 | tg-6091565924236663621 |
| 35 | 😍 | image/png | 256x256 | 209.2 | tg-6091443534848597185 |
| 36 | 👍 | image/png | 256x256 | 280.1 | tg-6093505419798386577 |
| 37 | 👟 | image/png | 256x256 | 108.9 | tg-6093643679090612788 |
| 38 | 🔥 | image/png | 256x256 | 318.2 | tg-6091156089867343498 |
| 39 | 🌟 | video/webm | 362x512 | 79.0 | tg-6091663226720754641 |
| 40 | 🌟 | image/png | 181x256 | 245.2 | tg-6091296015606880236 |
| 41 | 😍 | image/png | 256x192 | 161.8 | tg-6091292261805463752 |
| 42 | 😘 | video/webm | 512x406 | 179.0 | tg-6091452030293909405 |
| 43 | ⭐ | video/webm | 512x512 | 37.6 | tg-6091602560307699039 |
| 44 | ⭐ | video/webm | 512x512 | 116.7 | tg-6093469088670029808 |
| 45 | 🥵 | image/png | 256x256 | 462.5 | tg-6093889381284715164 |
| 46 | 🥵 | image/png | 256x256 | 527.1 | tg-6091553108054252133 |
| 47 | 🌟 | video/webm | 512x384 | 80.6 | tg-6091487639867758481 |
| 48 | 🍖 | image/png | 256x256 | 228.9 | tg-6091565464675163670 |
| 49 | 🌟 | image/png | 256x256 | 170.2 | tg-6091389877822167504 |
| 50 | ✨ | image/png | 256x256 | 542.4 | tg-6093715447994128698 |
| 51 | 🥵 | image/png | 230x256 | 319.6 | tg-6091449659471961109 |
| 52 | 🌟 | video/webm | 384x512 | 34.1 | tg-6091162317569923963 |
| 53 | 🥵 | image/png | 256x256 | 206.4 | tg-6091443650812713214 |
| 54 | 🥵 | image/png | 256x256 | 189.1 | tg-6091414462214969358 |
| 55 | 😍 | image/png | 256x256 | 200.4 | tg-6093791666483763451 |
| 56 | 🥵 | image/png | 256x256 | 235.8 | tg-6093739946487585942 |
| 57 | ❤️ | image/png | 256x249 | 297.4 | tg-6091448705989219931 |
| 58 | 😍 | image/png | 256x183 | 270.8 | tg-6091286875916475049 |
| 59 | 🌟 | video/webm | 512x288 | 15.5 | tg-6093677454713429168 |
| 60 | 🥰 | image/png | 214x256 | 234.3 | tg-6093889943925430334 |
| 61 | 🥰 | image/png | 256x256 | 203.0 | tg-6091317524803098347 |
| 62 | 😃 | image/png | 241x256 | 311.1 | tg-6093809434763467242 |
| 63 | 😉 | image/png | 256x256 | 294.9 | tg-6093775538881567210 |
| 64 | ⭐ | video/webm | 512x512 | 27.8 | tg-6093574869419562569 |
| 65 | ⭐ | video/webm | 512x500 | 61.7 | tg-6091389014533741608 |
| 66 | 🥵 | image/png | 256x216 | 207.7 | tg-6093856619274181818 |
| 67 | 🥰 | image/png | 256x181 | 222.2 | tg-6091279071960897321 |
| 68 | 😔 | image/png | 256x198 | 255.7 | tg-6093745276541999296 |
| 69 | ✋ | image/png | 256x256 | 131.6 | tg-6091262459027396105 |
| 70 | 😋 | image/png | 256x256 | 178.8 | tg-6091475545239856284 |
| 71 | ❤ | image/png | 256x256 | 302.9 | tg-6093632263067539884 |
| 72 | 🌟 | image/png | 256x231 | 327.3 | tg-6091534734184160343 |
| 73 | 🤥 | image/png | 256x241 | 282.8 | tg-6091249226233158607 |
| 74 | ⭐ | image/png | 256x254 | 232.7 | tg-6091387111863229531 |
| 75 | 🌟 | image/png | 174x256 | 201.3 | tg-6091615956310694232 |
| 76 | 😊 | image/png | 256x251 | 276.3 | tg-6091139262185478449 |
| 77 | 😗 | image/png | 180x256 | 173.8 | tg-6093395730628614573 |
| 78 | ❤ | image/png | 256x256 | 243.0 | tg-6091583679631464796 |
| 79 | 💇 | image/png | 256x256 | 177.8 | tg-6091229864520587476 |
| 80 | 😈 | video/webm | 512x512 | 241.0 | tg-6091499184739851164 |
| 81 | ⭐ | image/png | 256x225 | 241.0 | tg-6093898044233751009 |
| 82 | 🥵 | image/png | 256x192 | 176.2 | tg-6091304352138402704 |
| 83 | 😝 | image/png | 256x256 | 245.5 | tg-6091137161946473614 |
| 84 | 🤲 | image/png | 256x256 | 263.2 | tg-6091373398032653497 |
| 85 | ❤ | image/png | 256x211 | 284.4 | tg-6091621178990927521 |
| 86 | 👍 | image/png | 256x256 | 284.8 | tg-6091381786103782046 |
| 87 | 👍 | image/png | 256x256 | 159.7 | tg-6093520967579998526 |
| 88 | 👍 | image/png | 256x256 | 275.4 | tg-6093630253022844962 |
| 89 | 🖖 | image/png | 256x256 | 378.4 | tg-6093915614944958577 |
| 90 | ❤ | image/png | 256x256 | 268.0 | tg-6093731704445344672 |
| 91 | 👉 | image/png | 256x256 | 274.2 | tg-6093379895084194339 |
| 92 | 💇 | image/png | 256x256 | 281.0 | tg-6091590366895544539 |
| 93 | 🌟 | video/webm | 512x358 | 20.6 | tg-6093676608604871467 |
| 94 | 👍 | image/png | 256x256 | 102.4 | tg-6096166590124945063 |
| 95 | 👏 | image/png | 256x256 | 416.4 | tg-6096007341327522095 |
| 96 | 🌟 | video/webm | 512x512 | 95.0 | tg-6093875800598125314 |
| 97 | 💋 | image/png | 256x256 | 245.8 | tg-6093458999791851559 |
| 98 | 🥛 | image/png | 256x256 | 270.5 | tg-6093689347477872785 |
| 99 | 🥵 | image/png | 256x256 | 315.2 | tg-6093471652765506260 |
| 100 | 🖖 | image/png | 256x256 | 239.4 | tg-6093836488762465539 |
| 101 | ❤ | image/png | 256x256 | 140.9 | tg-6093529145197730966 |
| 102 | 💵 | image/png | 256x256 | 295.2 | tg-6093580130754501618 |
| 103 | 🍥 | image/png | 256x256 | 327.3 | tg-6093542863323274190 |
| 104 | 🤍 | image/png | 256x256 | 168.8 | tg-6098177588302190422 |
| 105 | ✨ | image/png | 181x256 | 199.8 | tg-6100605992876120320 |
| 106 | 🌟 | image/png | 256x256 | 199.8 | tg-6071298987179122637 |
| 107 | 🌟 | image/png | 256x256 | 144.8 | tg-6068851336856741613 |
| 108 | 🌟 | image/png | 256x256 | 214.2 | tg-6068937158893247899 |
| 109 | 🌟 | image/png | 256x256 | 170.7 | tg-6071035031374011496 |
| 110 | 🌟 | image/png | 256x256 | 215.3 | tg-6070897476456425146 |
| 111 | 🌟 | image/png | 201x256 | 169.4 | tg-6068629514680803799 |
| 112 | 🌟 | image/png | 226x256 | 166.7 | tg-6068941638544137629 |
| 113 | ✨ | image/png | 239x256 | 224.7 | tg-6068798860946317495 |
| 114 | ✨ | image/png | 250x256 | 378.2 | tg-6068649421854221363 |
| 115 | ⚪ | image/png | 256x241 | 296.4 | tg-6068775762612199498 |
| 116 | 🥵 | image/png | 256x256 | 506.0 | tg-6071049685802425784 |
| 117 | 🌟 | video/webm | 512x512 | 164.6 | tg-6068601898041091978 |
| 118 | 🌟 | video/webm | 512x512 | 156.8 | tg-6068634161835421778 |
| 119 | 👍 | image/png | 256x256 | 216.7 | tg-6068835703175782586 |


## 33. `LLM小妹` — `LLM_Moe.json`

- 標題:`LLM小妹`;包 ID:`tg-368868674896920584`
- 張數:120;mimetype 分佈:image/png ×120
- 大小統計:合計 37,246,095 B(35.52 MB);平均 303.1 KB;最小 89.1 KB;最大 526.6 KB
- 來源 ID:tg- ×120

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 😀 | image/png | 256x256 | 202.0 | tg-6190277372348998034 |
| 2 | 😃 | image/png | 256x256 | 229.1 | tg-6192482670551768841 |
| 3 | 🤣 | image/png | 256x256 | 214.0 | tg-6190335689414942506 |
| 4 | 😅 | image/png | 256x256 | 271.4 | tg-6190432493682828389 |
| 5 | 😂 | image/png | 256x256 | 240.2 | tg-6190575245510844218 |
| 6 | 😭 | image/png | 256x256 | 256.5 | tg-6298602125500883879 |
| 7 | ☺️ | image/png | 256x256 | 208.7 | tg-6192656281719809474 |
| 8 | 🥲 | image/png | 256x256 | 150.2 | tg-6190636173916905304 |
| 9 | 😁 | image/png | 256x256 | 151.7 | tg-6190609935961698838 |
| 10 | 😄 | image/png | 256x256 | 246.0 | tg-6192483168767975594 |
| 11 | 😒 | image/png | 256x256 | 281.0 | tg-6190198838871990545 |
| 12 | 😙 | image/png | 256x256 | 170.7 | tg-6246964176082707208 |
| 13 | 🤠 | image/png | 256x256 | 137.8 | tg-6088929888058744259 |
| 14 | 🤤 | image/png | 256x256 | 381.3 | tg-6307716634513517546 |
| 15 | 🥰 | image/png | 256x256 | 335.5 | tg-6244245315755451180 |
| 16 | 🤥 | image/png | 256x256 | 343.0 | tg-6219652363083329139 |
| 17 | 😘 | image/png | 256x256 | 288.5 | tg-6190422473524128277 |
| 18 | 👺 | image/png | 256x256 | 351.4 | tg-6062106223862358488 |
| 19 | 😚 | image/png | 256x256 | 347.4 | tg-6190478286624137330 |
| 20 | 🤪 | image/png | 256x256 | 395.4 | tg-6190595354547724510 |
| 21 | 🤨 | image/png | 256x256 | 463.3 | tg-6190657554264104963 |
| 22 | 😛 | image/png | 256x256 | 440.2 | tg-6244793817438888576 |
| 23 | 🙂 | image/png | 256x256 | 475.2 | tg-6282606653678298715 |
| 24 | 🥵 | image/png | 256x256 | 196.9 | tg-6274014236595199293 |
| 25 | 😲 | image/png | 256x256 | 247.8 | tg-6329856220261786351 |
| 26 | 🤐 | image/png | 256x256 | 89.1 | tg-6311911791064523348 |
| 27 | 👽 | image/png | 256x256 | 104.2 | tg-6309745770337675006 |
| 28 | 🤧 | image/png | 256x256 | 200.1 | tg-6330067360854060957 |
| 29 | 😣 | image/png | 256x256 | 196.4 | tg-6330246645673895128 |
| 30 | 😬 | image/png | 256x256 | 199.6 | tg-6334812870219408273 |
| 31 | 🤒 | image/png | 256x256 | 278.9 | tg-6305106668787084898 |
| 32 | 😑 | image/png | 256x256 | 255.0 | tg-6199582522074996122 |
| 33 | 😇 | image/png | 256x256 | 311.0 | tg-6282950693443608543 |
| 34 | 😤 | image/png | 256x256 | 306.9 | tg-6298697095817732779 |
| 35 | 😢 | image/png | 256x256 | 375.5 | tg-6339127946552287184 |
| 36 | 😫 | image/png | 256x256 | 242.4 | tg-6275851172632863404 |
| 37 | 😕 | image/png | 256x256 | 362.5 | tg-6057387643941954254 |
| 38 | 🥸 | image/png | 256x256 | 192.7 | tg-6280441028088439712 |
| 39 | 😟 | image/png | 256x256 | 231.9 | tg-6264571871254027712 |
| 40 | 😺 | image/png | 256x256 | 275.7 | tg-6089268786748203220 |
| 41 | 🧐 | image/png | 256x256 | 279.9 | tg-6190654887089413857 |
| 42 | 🤓 | image/png | 256x256 | 294.9 | tg-6190584518345236594 |
| 43 | 😎 | image/png | 256x256 | 318.1 | tg-6190735812863204510 |
| 44 | 🥱 | image/png | 256x256 | 304.3 | tg-6298436876634171068 |
| 45 | 💀 | image/png | 256x256 | 233.7 | tg-6280648981814979316 |
| 46 | 🤩 | image/png | 256x256 | 267.4 | tg-6190710691599492094 |
| 47 | ☹️ | image/png | 256x256 | 355.8 | tg-6190242445674946620 |
| 48 | 🥳 | image/png | 256x256 | 203.8 | tg-6190534494861140375 |
| 49 | 😶 | image/png | 256x256 | 372.0 | tg-6265048157357350721 |
| 50 | 👿 | image/png | 256x256 | 243.8 | tg-6249020430330371155 |
| 51 | 😝 | image/png | 256x256 | 281.8 | tg-6210558156381100990 |
| 52 | 😯 | image/png | 256x256 | 333.4 | tg-6339221508119863541 |
| 53 | 😏 | image/png | 256x256 | 248.7 | tg-6192494361452748149 |
| 54 | 🙂‍↕️ | image/png | 256x256 | 300.1 | tg-6264650271587049423 |
| 55 | 😗 | image/png | 256x256 | 385.3 | tg-6273759437660364993 |
| 56 | 😍 | image/png | 256x256 | 274.0 | tg-6307410278791258715 |
| 57 | 😊 | image/png | 256x256 | 314.5 | tg-6278242966905560922 |
| 58 | 🫡 | image/png | 256x256 | 420.5 | tg-6278506016472571903 |
| 59 | 🙂‍↔️ | image/png | 256x256 | 234.9 | tg-6192666185914391992 |
| 60 | 😌 | image/png | 256x256 | 246.1 | tg-6215135955863478962 |
| 61 | 😔 | image/png | 256x256 | 198.1 | tg-6190492498670919664 |
| 62 | 🥹 | image/png | 256x256 | 415.0 | tg-6248867770012802744 |
| 63 | 🤯 | image/png | 256x256 | 320.1 | tg-6273617484696265378 |
| 64 | 😳 | image/png | 256x256 | 337.2 | tg-6255818878228636782 |
| 65 | 😦 | image/png | 256x256 | 344.5 | tg-6264779051886452870 |
| 66 | 🤔 | image/png | 256x256 | 327.2 | tg-6226472698134928720 |
| 67 | 🥺 | image/png | 256x256 | 276.5 | tg-6052912936559584917 |
| 68 | 😉 | image/png | 256x256 | 399.7 | tg-6273916027873010367 |
| 69 | 🫢 | image/png | 256x256 | 474.4 | tg-6226507272621662317 |
| 70 | 😶‍🌫️ | image/png | 256x256 | 387.0 | tg-6255897080993161088 |
| 71 | 😩 | image/png | 256x256 | 401.7 | tg-6296575661146382721 |
| 72 | 🤭 | image/png | 256x256 | 310.5 | tg-6337017129040093743 |
| 73 | 🫤 | image/png | 256x256 | 329.1 | tg-6307295143602953648 |
| 74 | 😡 | image/png | 256x256 | 351.7 | tg-6273868753167983708 |
| 75 | 🫨 | image/png | 256x256 | 389.4 | tg-6307537658931322681 |
| 76 | 😸 | image/png | 256x256 | 263.7 | tg-6066767680717726217 |
| 77 | 😜 | image/png | 256x256 | 414.7 | tg-6089387168931782745 |
| 78 | 🫣 | image/png | 256x256 | 337.2 | tg-6089170316033007167 |
| 79 | 🥶 | image/png | 256x256 | 294.9 | tg-6255736363316946144 |
| 80 | 🙄 | image/png | 256x256 | 295.9 | tg-6336788134268772213 |
| 81 | 😆 | image/png | 256x256 | 318.5 | tg-6337000516106593019 |
| 82 | 🤡 | image/png | 256x256 | 293.8 | tg-6089217002327516899 |
| 83 | 👻 | image/png | 256x256 | 290.4 | tg-6088983553675110257 |
| 84 | 😋 | image/png | 256x256 | 343.9 | tg-6089176479311078557 |
| 85 | 🤫 | image/png | 256x256 | 359.9 | tg-6089155266467603523 |
| 86 | 😹 | image/png | 256x256 | 460.4 | tg-6307711914344456031 |
| 87 | ☠️ | image/png | 256x256 | 312.4 | tg-6332491491935526678 |
| 88 | 😻 | image/png | 256x256 | 472.7 | tg-6062292114341897131 |
| 89 | 🙁 | image/png | 256x256 | 526.6 | tg-6190203932703202135 |
| 90 | 🤖 | image/png | 256x256 | 344.4 | tg-6330011702372869272 |
| 91 | 😱 | image/png | 256x256 | 339.8 | tg-6190351104052567745 |
| 92 | 😨 | image/png | 256x256 | 301.7 | tg-6330275361825235066 |
| 93 | 😠 | image/png | 256x256 | 334.4 | tg-6222199441898610407 |
| 94 | 😐 | image/png | 256x256 | 328.3 | tg-6264518166982959597 |
| 95 | 🫠 | image/png | 256x256 | 288.8 | tg-6264683884001109032 |
| 96 | 🎃 | image/png | 256x256 | 304.6 | tg-6246546486218204581 |
| 97 | 😥 | image/png | 256x256 | 291.9 | tg-6246948731380309752 |
| 98 | 👾 | image/png | 256x256 | 309.7 | tg-6206365503796029216 |
| 99 | 😰 | image/png | 256x256 | 317.4 | tg-6190673626031726676 |
| 100 | 😞 | image/png | 256x256 | 305.5 | tg-6224436295226105765 |
| 101 | 🙃 | image/png | 256x256 | 241.0 | tg-6219665110546259999 |
| 102 | 😓 | image/png | 256x256 | 342.6 | tg-6190480056150663697 |
| 103 | 🤬 | image/png | 256x256 | 335.5 | tg-6221953490596405007 |
| 104 | 🤗 | image/png | 256x256 | 251.8 | tg-6190219420355273654 |
| 105 | 😧 | image/png | 256x256 | 232.7 | tg-6199527606623150523 |
| 106 | 😮 | image/png | 256x256 | 238.6 | tg-6197180239492162326 |
| 107 | 🤑 | image/png | 256x256 | 353.4 | tg-6201461218079679042 |
| 108 | 🥴 | image/png | 256x256 | 323.7 | tg-6073257629705052799 |
| 109 | 😷 | image/png | 256x256 | 318.3 | tg-6057815461339341821 |
| 110 | 🫥 | image/png | 256x256 | 251.4 | tg-6210892029958823554 |
| 111 | 🤢 | image/png | 256x256 | 213.1 | tg-6057537856128163541 |
| 112 | 💩 | image/png | 256x256 | 281.7 | tg-6055172776552047513 |
| 113 | 🤕 | image/png | 256x256 | 279.2 | tg-6203777966388812949 |
| 114 | 😵 | image/png | 256x256 | 340.1 | tg-6201751991660584749 |
| 115 | 😮‍💨 | image/png | 256x256 | 341.6 | tg-6201929262140760512 |
| 116 | 😈 | image/png | 256x256 | 287.0 | tg-6201481382951134635 |
| 117 | 👹 | image/png | 256x256 | 430.2 | tg-6204193886726794214 |
| 118 | 😪 | image/png | 256x256 | 310.0 | tg-6057642073509601254 |
| 119 | 😵‍💫 | image/png | 256x256 | 273.5 | tg-6057699239524313153 |
| 120 | 😴 | image/png | 256x256 | 453.8 | tg-6055583469914823902 |


## 34. `[HAL♂] :: @fStikBot` — `cd82afff_by_fStikBot.json`

- 標題:`[HAL♂] :: @fStikBot`;包 ID:`tg-381568008427929604`
- 張數:28;mimetype 分佈:image/png ×26;video/webm ×2
- 大小統計:合計 4,810,661 B(4.59 MB);平均 167.8 KB;最小 34.1 KB;最大 307.1 KB
- 來源 ID:tg- ×28

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🌟 | image/png | 256x191 | 222.5 | tg-6197443250404464782 |
| 2 | 🍏 | image/png | 256x256 | 285.5 | tg-6197243817893041958 |
| 3 | 🌟 | image/png | 256x179 | 143.7 | tg-6204083660686104768 |
| 4 | 🌟 | image/png | 256x254 | 267.0 | tg-6226384586880849364 |
| 5 | 🌟 | video/webm | 378x512 | 72.4 | tg-6097955452593644309 |
| 6 | 🌟 | video/webm | 512x512 | 226.9 | tg-6070991755283537444 |
| 7 | 🌟 | image/png | 200x256 | 241.9 | tg-6249235483637849315 |
| 8 | 🌟 | image/png | 256x86 | 54.0 | tg-6300768966566485368 |
| 9 | 🌟 | image/png | 256x143 | 155.7 | tg-6052999192387786986 |
| 10 | 🌟 | image/png | 256x83 | 34.1 | tg-6107087957519243954 |
| 11 | 🌟 | image/png | 195x256 | 307.1 | tg-6147612777843268513 |
| 12 | 🌟 | image/png | 256x138 | 191.6 | tg-6154645460372952494 |
| 13 | 🌟 | image/png | 239x256 | 246.7 | tg-6199731312627031352 |
| 14 | 🌟 | image/png | 256x203 | 279.5 | tg-6251310481122794594 |
| 15 | 🌟 | image/png | 256x203 | 295.5 | tg-6309868211265346292 |
| 16 | 🌟 | image/png | 248x256 | 260.8 | tg-6152040137506168060 |
| 17 | 🌟 | image/png | 256x256 | 187.7 | tg-6287194357355256287 |
| 18 | 🌟 | image/png | 256x231 | 94.6 | tg-6142927097372351230 |
| 19 | 🌟 | image/png | 256x231 | 103.7 | tg-6143229540379400600 |
| 20 | 🌟 | image/png | 256x256 | 104.0 | tg-6334687577433446021 |
| 21 | 🌟 | image/png | 256x255 | 169.2 | tg-6158942046871623833 |
| 22 | 🌟 | image/png | 256x255 | 134.1 | tg-6194779863874804509 |
| 23 | 🌟 | image/png | 256x256 | 112.4 | tg-6203817742080941296 |
| 24 | 🌟 | image/png | 256x100 | 114.2 | tg-6120787275400879341 |
| 25 | 🌟 | image/png | 256x115 | 63.0 | tg-6154614553788292428 |
| 26 | 🌟 | image/png | 256x254 | 122.5 | tg-6242354121395937162 |
| 27 | 🌟 | image/png | 256x88 | 105.8 | tg-6278458484069507475 |
| 28 | 🌟 | image/png | 256x256 | 101.7 | tg-6283034144658169491 |


## 35. `自用2` — `zhiyong2.json`

- 標題:`自用2`;包 ID:`tg-3518399408876027910`
- 張數:56;mimetype 分佈:image/png ×56
- 大小統計:合計 12,333,450 B(11.76 MB);平均 215.1 KB;最小 92.1 KB;最大 397.5 KB
- 來源 ID:tg- ×56

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🤡 | image/png | 256x239 | 151.5 | tg-6055151988910339442 |
| 2 | 🤡 | image/png | 256x182 | 125.1 | tg-6055101222396890636 |
| 3 | 8️⃣ | image/png | 256x144 | 135.9 | tg-6055459834986237553 |
| 4 | 👉 | image/png | 256x236 | 212.9 | tg-6307729485055659811 |
| 5 | 😎 | image/png | 189x256 | 190.3 | tg-6077648658239590017 |
| 6 | 🌚 | image/png | 256x232 | 383.6 | tg-6143022647509781998 |
| 7 | ☠️ | image/png | 256x138 | 219.0 | tg-6199600200160383260 |
| 8 | 💼 | image/png | 256x252 | 275.7 | tg-6257897187133361541 |
| 9 | 🥱 | image/png | 256x209 | 257.0 | tg-6264902691109998215 |
| 10 | 🐮 | image/png | 256x256 | 290.9 | tg-6320836909199266229 |
| 11 | 🚑 | image/png | 256x256 | 388.6 | tg-6107093090005160449 |
| 12 | 😣 | image/png | 255x256 | 397.5 | tg-6154178962500095714 |
| 13 | 😣 | image/png | 256x160 | 169.2 | tg-6215487683620245589 |
| 14 | 💼 | image/png | 256x256 | 229.3 | tg-6325373502765403792 |
| 15 | 😵 | image/png | 256x256 | 373.1 | tg-6131930168618389629 |
| 16 | 🍌 | image/png | 256x250 | 191.3 | tg-6143444421888184882 |
| 17 | 🌞 | image/png | 252x256 | 201.5 | tg-6163723775696178883 |
| 18 | 🌧 | image/png | 256x256 | 262.9 | tg-6210612741120462963 |
| 19 | 🙃 | image/png | 256x256 | 185.0 | tg-6231075279578600350 |
| 20 | 🚗 | image/png | 256x256 | 208.7 | tg-6239803649556485351 |
| 21 | 🪢 | image/png | 256x256 | 176.6 | tg-6093665604898657139 |
| 22 | 🫥 | image/png | 256x256 | 167.4 | tg-6102538066734355490 |
| 23 | 🫥 | image/png | 256x256 | 306.1 | tg-6100222452296586243 |
| 24 | 🧑‍💻 | image/png | 256x256 | 232.3 | tg-6109375014719460381 |
| 25 | 🫥 | image/png | 256x256 | 271.0 | tg-6120822352398784993 |
| 26 | 🫥 | image/png | 256x256 | 191.8 | tg-6172226715725600409 |
| 27 | 😺 | image/png | 256x256 | 92.1 | tg-6305379205936847105 |
| 28 | 1️⃣ | image/png | 256x256 | 277.0 | tg-6325438240807459308 |
| 29 | 🫥 | image/png | 256x256 | 190.2 | tg-6327673320313460602 |
| 30 | 😎 | image/png | 256x256 | 172.0 | tg-6082661602333563804 |
| 31 | 🫥 | image/png | 256x256 | 177.3 | tg-6098310496065165012 |
| 32 | 🫥 | image/png | 256x256 | 158.3 | tg-6129426589231880020 |
| 33 | 🫥 | image/png | 256x256 | 158.5 | tg-6156973367007123219 |
| 34 | 🫥 | image/png | 256x256 | 222.3 | tg-6159199208038473695 |
| 35 | 🫥 | image/png | 256x256 | 160.1 | tg-6172727229739441910 |
| 36 | 🫥 | image/png | 256x256 | 164.9 | tg-6174625420600679524 |
| 37 | 🐱 | image/png | 256x256 | 172.1 | tg-6176861904560986356 |
| 38 | 🫥 | image/png | 256x256 | 275.4 | tg-6183859346884007743 |
| 39 | 🫥 | image/png | 256x256 | 233.4 | tg-6199336613722462663 |
| 40 | 🫥 | image/png | 256x256 | 261.8 | tg-6240169954432260587 |
| 41 | 🫥 | image/png | 256x256 | 147.2 | tg-6253684790583633530 |
| 42 | 🫥 | image/png | 256x256 | 235.0 | tg-6309910954779877268 |
| 43 | 🫥 | image/png | 256x256 | 194.8 | tg-6071192051083387300 |
| 44 | 🫥 | image/png | 256x256 | 209.8 | tg-6179483204706113721 |
| 45 | 🫥 | image/png | 256x256 | 300.0 | tg-6332560679563697634 |
| 46 | 🫥 | image/png | 256x256 | 226.8 | tg-6127578232876177908 |
| 47 | 🫥 | image/png | 256x256 | 158.0 | tg-6165835735669676845 |
| 48 | 🫥 | image/png | 256x256 | 191.7 | tg-6138727925026922570 |
| 49 | 👹 | image/png | 256x256 | 226.7 | tg-6158747471968215566 |
| 50 | 🆘 | image/png | 256x256 | 212.9 | tg-6167829519618022826 |
| 51 | 🫥 | image/png | 256x256 | 190.1 | tg-6165607788870376976 |
| 52 | 👎 | image/png | 256x256 | 141.0 | tg-6165961956168572458 |
| 53 | 🐛 | image/png | 256x256 | 174.2 | tg-6192771034656022575 |
| 54 | 🫥 | image/png | 256x256 | 143.5 | tg-6208737622823542827 |
| 55 | 👹 | image/png | 256x256 | 221.7 | tg-6228507975762321481 |
| 56 | 🐛 | image/png | 256x256 | 161.6 | tg-6228478447862161194 |


## 36. `古明地歌の自用` — `KomeijiQualia.json`

- 標題:`古明地歌の自用`;包 ID:`tg-5908624656998334463`
- 張數:55;mimetype 分佈:image/png ×55
- 大小統計:合計 12,610,477 B(12.03 MB);平均 223.9 KB;最小 67.0 KB;最大 421.4 KB
- 來源 ID:tg- ×55

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🐉 | image/png | 256x256 | 235.8 | tg-6251023521472841667 |
| 2 | 🔨 | image/png | 256x256 | 371.6 | tg-6251162802967283518 |
| 3 | 🤪 | image/png | 256x256 | 130.0 | tg-6251199645196749131 |
| 4 | 🥶 | image/png | 256x256 | 292.2 | tg-6253306043187595085 |
| 5 | 🫡 | image/png | 256x256 | 360.1 | tg-6251081567955847641 |
| 6 | 🤯 | image/png | 256x256 | 272.4 | tg-6251407079232244260 |
| 7 | 😕 | image/png | 256x256 | 268.3 | tg-6253342833877452764 |
| 8 | 🥱 | image/png | 256x256 | 234.9 | tg-6253538194759878608 |
| 9 | 😕 | image/png | 256x256 | 399.4 | tg-6253603946414212740 |
| 10 | 🥴 | image/png | 256x256 | 236.1 | tg-6251334880831998010 |
| 11 | 👴 | image/png | 256x256 | 230.0 | tg-6251234266928121924 |
| 12 | 🧐 | image/png | 256x256 | 240.4 | tg-6258192354465810067 |
| 13 | 😦 | image/png | 256x256 | 340.1 | tg-6258206154195732570 |
| 14 | 😡 | image/png | 256x166 | 228.5 | tg-6260254965265073817 |
| 15 | 🤯 | image/png | 256x159 | 231.2 | tg-6258159162958547012 |
| 16 | 🥱 | image/png | 200x256 | 221.7 | tg-6053077210468714790 |
| 17 | 😭 | image/png | 256x242 | 202.3 | tg-6082534217898527163 |
| 18 | 🥰 | image/png | 256x256 | 108.8 | tg-6203802821364551839 |
| 19 | 🖼 | image/png | 256x256 | 112.1 | tg-6201696998899323376 |
| 20 | 😡 | image/png | 256x256 | 230.4 | tg-6204211633531655163 |
| 21 | 😫 | image/png | 256x256 | 211.0 | tg-6201563270797595111 |
| 22 | 🥰 | image/png | 256x256 | 88.8 | tg-6204004186611258587 |
| 23 | 😨 | image/png | 256x256 | 196.7 | tg-6204078979171750111 |
| 24 | 😡 | image/png | 256x256 | 249.9 | tg-6204255918939443793 |
| 25 | 🤮 | image/png | 256x256 | 228.2 | tg-6206361616850621914 |
| 26 | ❤ | image/png | 256x256 | 308.5 | tg-6204098950769676631 |
| 27 | 😫 | image/png | 256x256 | 244.2 | tg-6203965463186117843 |
| 28 | 🐱 | image/png | 256x256 | 82.1 | tg-6204243437764481863 |
| 29 | 🐱 | image/png | 256x256 | 67.0 | tg-6204017616973992387 |
| 30 | 😊 | image/png | 256x256 | 247.0 | tg-6206465340310819163 |
| 31 | ❤ | image/png | 256x256 | 274.4 | tg-6204017041448375003 |
| 32 | 🥲 | image/png | 256x256 | 218.6 | tg-6204097060984066810 |
| 33 | 😉 | image/png | 256x256 | 334.8 | tg-6206322008662217715 |
| 34 | 😡 | image/png | 256x256 | 155.0 | tg-6206203703788049379 |
| 35 | 🫥 | image/png | 256x256 | 132.6 | tg-6203790499103381641 |
| 36 | 🎩 | image/png | 256x256 | 133.1 | tg-6212749629084144898 |
| 37 | 👍 | image/png | 256x256 | 155.5 | tg-6318573259570810848 |
| 38 | 🙄 | image/png | 256x256 | 232.6 | tg-6059964555600073332 |
| 39 | 🥰 | image/png | 256x256 | 303.1 | tg-6084428465979790262 |
| 40 | 👍 | image/png | 256x256 | 421.4 | tg-6127542258230104941 |
| 41 | 🙂 | image/png | 256x256 | 138.4 | tg-6147595198542125810 |
| 42 | ❤ | image/png | 256x256 | 117.8 | tg-6143344937560713707 |
| 43 | 🥰 | image/png | 256x256 | 205.8 | tg-6174791305122551736 |
| 44 | 🤫 | image/png | 256x256 | 172.7 | tg-6206344750514052277 |
| 45 | 🤪 | image/png | 256x256 | 229.2 | tg-6228915568158709883 |
| 46 | 😡 | image/png | 256x256 | 282.6 | tg-6318652630566443872 |
| 47 | 🥱 | image/png | 256x256 | 166.4 | tg-6332606786037620078 |
| 48 | 😌 | image/png | 256x256 | 201.4 | tg-6095795217187741194 |
| 49 | 😡 | image/png | 256x256 | 165.5 | tg-6100239133949566869 |
| 50 | 😌 | image/png | 256x256 | 207.1 | tg-6149987654239788248 |
| 51 | 🫣 | image/png | 256x256 | 208.4 | tg-6194890983268688243 |
| 52 | ❤ | image/png | 256x256 | 308.9 | tg-6226770833289781000 |
| 53 | 🐷 | image/png | 256x256 | 149.1 | tg-6321265164683322155 |
| 54 | ❤ | image/png | 256x256 | 297.8 | tg-6325386666840170125 |
| 55 | ❤ | image/png | 256x256 | 232.8 | tg-6057472959172322741 |


## 37. `しろいぬシンドローム @LuoDian_Stickers` — `Shiroinu_shindoromu_By_LuoDian.json`

- 標題:`しろいぬシンドローム @LuoDian_Stickers`;包 ID:`tg-5000801319481507844`
- 張數:86;mimetype 分佈:image/png ×86
- 大小統計:合計 17,054,227 B(16.26 MB);平均 193.7 KB;最小 46.6 KB;最大 331.0 KB
- 來源 ID:tg- ×86

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 😴 | image/png | 256x228 | 122.6 | tg-6077984636351285507 |
| 2 | 😭 | image/png | 203x256 | 243.4 | tg-6077654392020928581 |
| 3 | 😚 | image/png | 256x160 | 205.0 | tg-6078104599082829617 |
| 4 | 🤔 | image/png | 256x211 | 181.2 | tg-6077992092414511006 |
| 5 | 😆 | image/png | 225x256 | 217.0 | tg-6077756092551531253 |
| 6 | 🥹 | image/png | 178x256 | 103.3 | tg-6078073778397513592 |
| 7 | 😝 | image/png | 196x256 | 185.6 | tg-6077892363273897967 |
| 8 | 😒 | image/png | 217x256 | 133.8 | tg-6078011836379170515 |
| 9 | 🧐 | image/png | 256x240 | 144.7 | tg-6077763707528546168 |
| 10 | 🤨 | image/png | 216x256 | 181.5 | tg-6077936232069859828 |
| 11 | ☺️ | image/png | 197x256 | 144.8 | tg-6077844693431879872 |
| 12 | 😊 | image/png | 196x256 | 206.4 | tg-6078041024976914100 |
| 13 | 😇 | image/png | 175x256 | 123.9 | tg-6077896220154529667 |
| 14 | 🙂 | image/png | 145x256 | 161.3 | tg-6077999037376628668 |
| 15 | 😣 | image/png | 227x256 | 146.3 | tg-6075840786245617889 |
| 16 | 😉 | image/png | 192x256 | 147.4 | tg-6078061894223005466 |
| 17 | 😌 | image/png | 193x256 | 153.1 | tg-6077726246823790383 |
| 18 | 😍 | image/png | 256x190 | 187.5 | tg-6077800695786899338 |
| 19 | 🤯 | image/png | 221x256 | 246.3 | tg-6077872984381458331 |
| 20 | 😴 | image/png | 256x211 | 330.3 | tg-6077689159781189512 |
| 21 | 😣 | image/png | 183x256 | 233.5 | tg-6077626766791280808 |
| 22 | 😢 | image/png | 172x256 | 189.2 | tg-6077888987429603226 |
| 23 | 🫣 | image/png | 193x256 | 270.6 | tg-6078011784839563166 |
| 24 | 😋 | image/png | 256x240 | 256.9 | tg-6077811940011280204 |
| 25 | 😄 | image/png | 176x256 | 213.1 | tg-6077944246478834346 |
| 26 | 😝 | image/png | 182x256 | 160.1 | tg-6077945513494185908 |
| 27 | 😄 | image/png | 175x256 | 140.3 | tg-6077882682417612511 |
| 28 | 🥰 | image/png | 256x221 | 259.9 | tg-6075411731897649172 |
| 29 | 🐶 | image/png | 256x242 | 298.9 | tg-6077613100205344565 |
| 30 | 🥰 | image/png | 138x256 | 169.6 | tg-6077852209624647661 |
| 31 | ‼️ | image/png | 205x256 | 283.5 | tg-6077888029651897360 |
| 32 | 🫣 | image/png | 183x256 | 243.1 | tg-6077789537461864919 |
| 33 | 😀 | image/png | 204x256 | 230.1 | tg-6077715101383657495 |
| 34 | 🤩 | image/png | 228x256 | 271.6 | tg-6077646996087245050 |
| 35 | 😮 | image/png | 228x256 | 241.8 | tg-6077883442626824504 |
| 36 | 😏 | image/png | 231x256 | 198.4 | tg-6077827668181518083 |
| 37 | 😘 | image/png | 168x256 | 175.7 | tg-6077650883032647664 |
| 38 | 🫣 | image/png | 194x256 | 234.0 | tg-6078098259711101083 |
| 39 | 😝 | image/png | 146x256 | 175.3 | tg-6077874023763544319 |
| 40 | 😝 | image/png | 256x173 | 201.1 | tg-6077753013059979162 |
| 41 | 😯 | image/png | 217x256 | 197.1 | tg-6077981861802412033 |
| 42 | 🙁 | image/png | 200x256 | 163.2 | tg-6077976909705119622 |
| 43 | 😭 | image/png | 186x256 | 144.2 | tg-6078153982616799439 |
| 44 | 😣 | image/png | 217x256 | 215.6 | tg-6077957646776797020 |
| 45 | 😙 | image/png | 177x256 | 172.0 | tg-6077640545046366061 |
| 46 | 😫 | image/png | 216x256 | 247.9 | tg-6078074302383523632 |
| 47 | 🔞 | image/png | 210x256 | 211.0 | tg-6077813520559245377 |
| 48 | 🚺 | image/png | 200x256 | 198.4 | tg-6077821272975214536 |
| 49 | 🤕 | image/png | 188x256 | 206.2 | tg-6077973976242456528 |
| 50 | 🔞 | image/png | 233x256 | 285.6 | tg-6078141132074649632 |
| 51 | 🪥 | image/png | 235x256 | 212.5 | tg-6077899767797516470 |
| 52 | 😠 | image/png | 192x256 | 197.8 | tg-6077748919956145844 |
| 53 | 😲 | image/png | 256x230 | 331.0 | tg-6077677662153738100 |
| 54 | ❓ | image/png | 235x256 | 219.6 | tg-6077655835129939632 |
| 55 | 🤯 | image/png | 217x256 | 223.8 | tg-6078086998306851064 |
| 56 | 😳 | image/png | 256x189 | 171.8 | tg-6077914301966846621 |
| 57 | ❤️ | image/png | 188x256 | 193.1 | tg-6077747640055892529 |
| 58 | 😭 | image/png | 182x256 | 286.7 | tg-6078050409480456102 |
| 59 | 🙁 | image/png | 195x256 | 175.7 | tg-6077735214715504851 |
| 60 | 🐶 | image/png | 256x189 | 161.3 | tg-6077795408682157927 |
| 61 | 🐶 | image/png | 256x190 | 203.9 | tg-6077894506462578372 |
| 62 | ❤️ | image/png | 256x193 | 194.8 | tg-6077828428390729417 |
| 63 | 😱 | image/png | 256x189 | 155.3 | tg-6077932568462755614 |
| 64 | 😓 | image/png | 219x256 | 216.8 | tg-6077913125145806382 |
| 65 | 🤗 | image/png | 256x206 | 176.8 | tg-6077827169965311900 |
| 66 | 🤔 | image/png | 157x256 | 263.4 | tg-6078118514776868752 |
| 67 | 🐰 | image/png | 199x256 | 269.6 | tg-6078011419767343045 |
| 68 | ❗️ | image/png | 256x205 | 110.8 | tg-6077711064114399081 |
| 69 | 😣 | image/png | 214x256 | 217.4 | tg-6077887084759090986 |
| 70 | 😖 | image/png | 256x178 | 134.2 | tg-6077687841226229737 |
| 71 | 💕 | image/png | 256x189 | 182.9 | tg-6077962701953304436 |
| 72 | 🐶 | image/png | 256x191 | 46.6 | tg-6077726096499935194 |
| 73 | 🤗 | image/png | 234x256 | 114.2 | tg-6078164256178571383 |
| 74 | 😭 | image/png | 256x192 | 103.1 | tg-6077779375569242130 |
| 75 | 😃 | image/png | 220x256 | 106.0 | tg-6078136600884151795 |
| 76 | 🫢 | image/png | 148x256 | 94.5 | tg-6078104070801852227 |
| 77 | 🈲 | image/png | 182x256 | 100.7 | tg-6077629047418914558 |
| 78 | 🤐 | image/png | 256x222 | 164.8 | tg-6077646888713062463 |
| 79 | 🐶 | image/png | 202x256 | 130.2 | tg-6077620891276020039 |
| 80 | 🤕 | image/png | 200x256 | 172.8 | tg-6077616901251402000 |
| 81 | 😇 | image/png | 198x256 | 165.1 | tg-6077773122096859438 |
| 82 | ⁉️ | image/png | 256x233 | 270.5 | tg-6077877704550516514 |
| 83 | 😴 | image/png | 256x197 | 221.4 | tg-6077789528871930242 |
| 84 | 😉 | image/png | 238x256 | 247.3 | tg-6077628188425455571 |
| 85 | 😴 | image/png | 224x256 | 140.9 | tg-6077849482320416386 |
| 86 | 😊 | image/png | 256x252 | 223.6 | tg-6143166481669556565 |


## 38. `忆忆怪话集` — `fuckyiyi.json`

- 標題:`忆忆怪话集`;包 ID:`tg-4784006252441108488`
- 張數:114;mimetype 分佈:image/png ×114
- 大小統計:合計 12,828,940 B(12.23 MB);平均 109.9 KB;最小 42.3 KB;最大 469.2 KB
- 來源 ID:tg- ×114

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🇦🇼 | image/png | 256x155 | 70.2 | tg-6170150910786806753 |
| 2 | 🙂 | image/png | 229x256 | 186.9 | tg-6170246808816591740 |
| 3 | 🥹 | image/png | 256x256 | 95.5 | tg-6123116775467919076 |
| 4 | 🥹 | image/png | 256x256 | 70.9 | tg-6122786359338869976 |
| 5 | 😀 | image/png | 256x256 | 64.8 | tg-6118685236801838145 |
| 6 | 😀 | image/png | 256x256 | 294.6 | tg-6082322742298813096 |
| 7 | 😀 | image/png | 256x256 | 55.4 | tg-6082330159707332141 |
| 8 | 😀 | image/png | 256x256 | 61.0 | tg-6082356088424897917 |
| 9 | 😀 | image/png | 256x256 | 90.1 | tg-6082469492741380866 |
| 10 | 😀 | image/png | 256x256 | 141.2 | tg-6082145222710533393 |
| 11 | 😀 | image/png | 256x256 | 94.8 | tg-6082237225204982189 |
| 12 | 😀 | image/png | 256x256 | 63.5 | tg-6082255977032194904 |
| 13 | 😀 | image/png | 256x256 | 154.5 | tg-6082609981121634127 |
| 14 | 😀 | image/png | 256x256 | 52.0 | tg-6082217781888032492 |
| 15 | 😀 | image/png | 256x256 | 50.4 | tg-6082138479611878759 |
| 16 | 😀 | image/png | 256x256 | 190.5 | tg-6082188838103424779 |
| 17 | 😀 | image/png | 256x256 | 93.6 | tg-6082565115893259499 |
| 18 | 😀 | image/png | 256x256 | 110.7 | tg-6082579061652069369 |
| 19 | 😀 | image/png | 256x256 | 85.1 | tg-6082183190221429640 |
| 20 | 😀 | image/png | 256x256 | 98.3 | tg-6082505866819412701 |
| 21 | 😀 | image/png | 256x256 | 200.2 | tg-6082599415502085313 |
| 22 | 😀 | image/png | 256x256 | 98.8 | tg-6082316574725774501 |
| 23 | 😀 | image/png | 256x256 | 64.6 | tg-6082327578431987790 |
| 24 | 😀 | image/png | 256x256 | 75.7 | tg-6082541944544697159 |
| 25 | 😀 | image/png | 256x256 | 95.1 | tg-6082185384949718574 |
| 26 | 😀 | image/png | 256x256 | 335.1 | tg-6084709447035265116 |
| 27 | 😀 | image/png | 256x256 | 170.3 | tg-6082506846071955287 |
| 28 | 😀 | image/png | 256x256 | 74.9 | tg-6082369299744301447 |
| 29 | 😀 | image/png | 256x256 | 127.0 | tg-6082389636414445616 |
| 30 | 😀 | image/png | 256x256 | 74.0 | tg-6082369604686978984 |
| 31 | 😀 | image/png | 256x256 | 123.2 | tg-6082568723665788308 |
| 32 | 😀 | image/png | 256x256 | 126.0 | tg-6082522209169972988 |
| 33 | 😀 | image/png | 256x256 | 104.8 | tg-6082514147516358401 |
| 34 | 😀 | image/png | 256x256 | 50.5 | tg-6082620873158696855 |
| 35 | 😀 | image/png | 256x256 | 154.6 | tg-6082395584944152395 |
| 36 | 😀 | image/png | 256x256 | 59.3 | tg-6082249659135302583 |
| 37 | 😀 | image/png | 256x256 | 121.9 | tg-6082524163380092291 |
| 38 | 😀 | image/png | 256x256 | 125.4 | tg-6082149474728157225 |
| 39 | 😀 | image/png | 256x256 | 116.1 | tg-6082560765091389352 |
| 40 | 😀 | image/png | 256x256 | 81.1 | tg-6082343151983403693 |
| 41 | 😀 | image/png | 256x256 | 50.5 | tg-6082645436076663673 |
| 42 | 😀 | image/png | 256x256 | 58.2 | tg-6082285084025559888 |
| 43 | 😀 | image/png | 256x256 | 93.2 | tg-6082637619236183179 |
| 44 | 😀 | image/png | 256x256 | 64.6 | tg-6082478555122376442 |
| 45 | 😀 | image/png | 256x256 | 111.9 | tg-6084510800502857312 |
| 46 | 😀 | image/png | 256x256 | 88.8 | tg-6082384697202057041 |
| 47 | 😀 | image/png | 256x256 | 107.4 | tg-6082331856219413160 |
| 48 | 😀 | image/png | 256x256 | 48.9 | tg-6082253138058812764 |
| 49 | 😀 | image/png | 256x256 | 138.2 | tg-6082458025178701811 |
| 50 | 😀 | image/png | 256x256 | 64.5 | tg-6082648154790960268 |
| 51 | 😀 | image/png | 256x256 | 99.9 | tg-6082182765019667174 |
| 52 | 😀 | image/png | 256x256 | 95.8 | tg-6082652758995901872 |
| 53 | 😌 | image/png | 256x70 | 85.1 | tg-6244368143230176370 |
| 54 | 😀 | image/png | 256x98 | 137.4 | tg-6242536313908628799 |
| 55 | 😀 | image/png | 256x110 | 147.5 | tg-6242169394852531903 |
| 56 | 😀 | image/png | 256x32 | 46.6 | tg-6244780747853401776 |
| 57 | 😀 | image/png | 256x55 | 89.1 | tg-6244765547964141362 |
| 58 | 😀 | image/png | 256x120 | 140.4 | tg-6244436862706912169 |
| 59 | 😀 | image/png | 256x100 | 113.2 | tg-6244315027369627791 |
| 60 | 😽 | image/png | 255x256 | 384.9 | tg-6244551181851429708 |
| 61 | 😽 | image/png | 256x73 | 90.4 | tg-6242045729859178493 |
| 62 | 😽 | image/png | 256x121 | 128.3 | tg-6244685940745310835 |
| 63 | 😽 | image/png | 256x62 | 74.4 | tg-6244369869807029547 |
| 64 | 😻 | image/png | 256x51 | 51.9 | tg-6246820788599524428 |
| 65 | 😻 | image/png | 256x77 | 91.7 | tg-6247026161050718455 |
| 66 | 😻 | image/png | 256x55 | 57.1 | tg-6246693756351811003 |
| 67 | 😻 | image/png | 256x138 | 131.4 | tg-6246711958423211802 |
| 68 | 😻 | image/png | 256x74 | 100.2 | tg-6246974170471600153 |
| 69 | 😻 | image/png | 256x63 | 87.7 | tg-6246819955375869022 |
| 70 | 😻 | image/png | 256x38 | 42.3 | tg-6246735069642231135 |
| 71 | 😻 | image/png | 256x82 | 117.9 | tg-6246530521824759090 |
| 72 | 😻 | image/png | 256x87 | 131.0 | tg-6246540052357190323 |
| 73 | 😻 | image/png | 256x256 | 469.2 | tg-6246805739034119070 |
| 74 | 😻 | image/png | 256x182 | 208.3 | tg-6246493795559411414 |
| 75 | 😻 | image/png | 256x55 | 87.9 | tg-6246504640351833630 |
| 76 | 😻 | image/png | 256x122 | 106.2 | tg-6246570662589107474 |
| 77 | 😻 | image/png | 256x72 | 87.6 | tg-6247052033933709101 |
| 78 | 😻 | image/png | 256x110 | 133.7 | tg-6246858438282841150 |
| 79 | 😻 | image/png | 256x43 | 68.9 | tg-6246622477074568647 |
| 80 | 😻 | image/png | 256x76 | 82.2 | tg-6246865662417833040 |
| 81 | 😻 | image/png | 256x126 | 150.5 | tg-6246500031851924151 |
| 82 | 😻 | image/png | 256x134 | 169.6 | tg-6246635276077109459 |
| 83 | 😻 | image/png | 256x78 | 101.4 | tg-6246977438941711773 |
| 84 | 😻 | image/png | 256x69 | 77.7 | tg-6246594950629166828 |
| 85 | 😻 | image/png | 256x103 | 122.0 | tg-6246753233058925785 |
| 86 | 😻 | image/png | 256x49 | 55.1 | tg-6246835881114603966 |
| 87 | 😻 | image/png | 256x68 | 80.6 | tg-6249097314539933342 |
| 88 | 😻 | image/png | 256x97 | 101.5 | tg-6246699541672758688 |
| 89 | 😻 | image/png | 256x63 | 62.6 | tg-6246822167284027679 |
| 90 | 😻 | image/png | 256x60 | 80.7 | tg-6246852665846795918 |
| 91 | 😻 | image/png | 256x142 | 116.4 | tg-6246724452483075387 |
| 92 | 😻 | image/png | 256x82 | 101.1 | tg-6246506182245092548 |
| 93 | 😻 | image/png | 256x46 | 50.0 | tg-6246963334269111903 |
| 94 | 😻 | image/png | 256x82 | 101.8 | tg-6246602544131347120 |
| 95 | 😻 | image/png | 256x39 | 51.2 | tg-6246639523799764312 |
| 96 | 😻 | image/png | 256x86 | 102.6 | tg-6246905691513031607 |
| 97 | 😻 | image/png | 256x140 | 164.3 | tg-6246519505233644916 |
| 98 | 😻 | image/png | 256x60 | 89.5 | tg-6246562081244450102 |
| 99 | 😻 | image/png | 256x149 | 119.0 | tg-6246547864902700447 |
| 100 | 😻 | image/png | 256x80 | 112.8 | tg-6246851450371051529 |
| 101 | 😻 | image/png | 256x52 | 83.6 | tg-6246565268110184424 |
| 102 | 😻 | image/png | 256x58 | 98.2 | tg-6246691394119798632 |
| 103 | 😻 | image/png | 256x101 | 94.9 | tg-6247049057521372959 |
| 104 | 😻 | image/png | 256x221 | 218.1 | tg-6246663738825379652 |
| 105 | 😻 | image/png | 256x51 | 66.1 | tg-6249234354061446101 |
| 106 | 😻 | image/png | 256x89 | 115.2 | tg-6246515210266349341 |
| 107 | 😻 | image/png | 256x116 | 102.9 | tg-6246770893964447178 |
| 108 | 😽 | image/png | 256x140 | 187.6 | tg-6266910064334867557 |
| 109 | 😽 | image/png | 256x78 | 99.0 | tg-6266823791326793081 |
| 110 | 😽 | image/png | 256x56 | 77.3 | tg-6266767733413646737 |
| 111 | 😽 | image/png | 256x71 | 75.3 | tg-6267052421025893772 |
| 112 | 😽 | image/png | 256x49 | 55.0 | tg-6267268466470817053 |
| 113 | 😽 | image/png | 256x121 | 150.2 | tg-6267298247774047990 |
| 114 | 🙂 | image/png | 256x172 | 77.7 | tg-6179171643483495816 |


## 39. `@HanaCS2` — `HanaCS2Video.json`

- 標題:`@HanaCS2`;包 ID:`tg-2343012562418794488`
- 張數:9;mimetype 分佈:video/webm ×9
- 大小統計:合計 1,230,131 B(1.17 MB);平均 133.5 KB;最小 16.3 KB;最大 234.2 KB
- 來源 ID:tg- ×9

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 😘 | video/webm | 512x512 | 234.2 | tg-6070910305523736357 |
| 2 | 😯 | video/webm | 512x512 | 16.3 | tg-6249039139207911737 |
| 3 | 😨 | video/webm | 512x512 | 170.8 | tg-6248866971148883556 |
| 4 | 😅 | video/webm | 512x512 | 180.0 | tg-6249005672822742674 |
| 5 | 🐷 | video/webm | 512x512 | 91.4 | tg-6091556217610574760 |
| 6 | 🐷 | video/webm | 512x512 | 61.9 | tg-6293918944700930870 |
| 7 | 🤩 | video/webm | 512x512 | 112.5 | tg-6316357322734049513 |
| 8 | 🥳 | video/webm | 512x512 | 187.3 | tg-6316482027109489974 |
| 9 | 💃 | video/webm | 512x512 | 146.9 | tg-6325464723575807930 |


## 40. `Thinking` — `ai_think_by_lolspbot.json`

- 標題:`Thinking`;包 ID:`tg-4095636326181765105`
- 張數:13;mimetype 分佈:video/webm ×13
- 大小統計:合計 290,901 B(0.28 MB);平均 21.9 KB;最小 5.3 KB;最大 39.1 KB
- 來源 ID:tg- ×13

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🙂 | video/webm | 512x160 | 28.7 | tg-6307326574173629035 |
| 2 | 🙂 | video/webm | 512x76 | 11.7 | tg-6307570936337931427 |
| 3 | 🙂 | video/webm | 512x266 | 30.0 | tg-6307301066362854785 |
| 4 | 🙂 | video/webm | 512x126 | 17.7 | tg-6307413031865293719 |
| 5 | 🙂 | video/webm | 512x262 | 15.8 | tg-6307615612587744854 |
| 6 | 🙂 | video/webm | 512x174 | 19.4 | tg-6305255467929050974 |
| 7 | 🙂 | video/webm | 512x178 | 14.2 | tg-6307518408887901472 |
| 8 | 🙂 | video/webm | 512x166 | 18.4 | tg-6307767869178388420 |
| 9 | 🙂 | video/webm | 512x262 | 32.0 | tg-6305483917239524972 |
| 10 | 🙂 | video/webm | 512x176 | 28.3 | tg-6305234602977926387 |
| 11 | 🙂 | video/webm | 512x164 | 23.4 | tg-6307572147518709024 |
| 12 | 🙂 | video/webm | 512x178 | 39.1 | tg-6305105380296892475 |
| 13 | 🙂 | video/webm | 512x144 | 5.3 | tg-6309956932404780763 |


## 41. `得卢，爱卢 :: @fStikBot` — `Unconscious_Apricot_Salamander_by_fStikBot.json`

- 標題:`得卢，爱卢 :: @fStikBot`;包 ID:`tg-1779971693129760761`
- 張數:16;mimetype 分佈:image/png ×16
- 大小統計:合計 3,460,314 B(3.30 MB);平均 211.2 KB;最小 120.6 KB;最大 340.8 KB
- 來源 ID:tg- ×16

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🌟 | image/png | 256x134 | 199.4 | tg-6147971669605489238 |
| 2 | 🌟 | image/png | 256x135 | 185.9 | tg-6147418267364366851 |
| 3 | 🌟 | image/png | 256x141 | 222.9 | tg-6149820992328832960 |
| 4 | 🌟 | image/png | 256x116 | 131.5 | tg-6150170671386204677 |
| 5 | 🌟 | image/png | 256x128 | 186.6 | tg-6149971333364062546 |
| 6 | 🌟 | image/png | 256x179 | 340.8 | tg-6150156764282100956 |
| 7 | 🌟 | image/png | 256x185 | 264.1 | tg-6150196814852136354 |
| 8 | 🌟 | image/png | 256x162 | 233.7 | tg-6150119595635121762 |
| 9 | 🌟 | image/png | 256x137 | 247.2 | tg-6149899242337999435 |
| 10 | 🌟 | image/png | 256x132 | 206.0 | tg-6147613748505879059 |
| 11 | 🌟 | image/png | 256x161 | 303.5 | tg-6149788015569933864 |
| 12 | 🌟 | image/png | 256x137 | 210.9 | tg-6149721928908152049 |
| 13 | 🌟 | image/png | 256x155 | 185.3 | tg-6147735588138130458 |
| 14 | 🌟 | image/png | 256x135 | 164.5 | tg-6147769277861601083 |
| 15 | 🌟 | image/png | 256x134 | 120.6 | tg-6147959068171442201 |
| 16 | 🌟 | image/png | 256x132 | 176.5 | tg-6150157773599414910 |


## 42. `宇佐紀ノノ_usagi` — `usagi_stickers.json`

- 標題:`宇佐紀ノノ_usagi`;包 ID:`tg-8247600302367178755`
- 張數:41;mimetype 分佈:image/png ×41
- 大小統計:合計 10,464,906 B(9.98 MB);平均 249.3 KB;最小 91.0 KB;最大 565.0 KB
- 來源 ID:tg- ×41

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | ❤️ | image/png | 222x256 | 290.0 | tg-6145720123194868448 |
| 2 | ❤️ | image/png | 256x198 | 206.6 | tg-6147645084587262656 |
| 3 | ❤️ | image/png | 256x180 | 186.7 | tg-6147526337331462772 |
| 4 | ❤️ | image/png | 202x256 | 307.5 | tg-6145566105667634126 |
| 5 | ❤️ | image/png | 220x256 | 308.2 | tg-6145350648633230300 |
| 6 | ❤️ | image/png | 256x256 | 312.7 | tg-6145296416081183606 |
| 7 | ❤️ | image/png | 238x256 | 245.7 | tg-6147780947287737009 |
| 8 | ❤️ | image/png | 197x256 | 237.5 | tg-6145644248302617622 |
| 9 | ❤️ | image/png | 256x227 | 226.8 | tg-6147414191440397011 |
| 10 | ❤️ | image/png | 256x218 | 233.4 | tg-6147512833954284240 |
| 11 | ❤️ | image/png | 233x256 | 267.9 | tg-6145290484731348070 |
| 12 | ❤️ | image/png | 256x98 | 91.0 | tg-6145444283215250111 |
| 13 | ❤️ | image/png | 250x256 | 288.0 | tg-6147510480312206093 |
| 14 | ❤️ | image/png | 256x228 | 215.9 | tg-6147571765200553197 |
| 15 | ❤️ | image/png | 256x226 | 228.7 | tg-6147919670436430721 |
| 16 | ❤️ | image/png | 193x256 | 226.9 | tg-6147544547992798049 |
| 17 | ❤️ | image/png | 256x225 | 215.4 | tg-6149821378875884494 |
| 18 | ❤️ | image/png | 256x226 | 240.5 | tg-6147794270276289425 |
| 19 | ❤️ | image/png | 254x256 | 271.0 | tg-6147729141392212896 |
| 20 | ❤️ | image/png | 256x221 | 241.0 | tg-6150051391554454062 |
| 21 | ❤️ | image/png | 224x256 | 208.2 | tg-6190720630153806646 |
| 22 | ❤️ | image/png | 256x226 | 236.3 | tg-6190532313017746095 |
| 23 | ❤️ | image/png | 256x162 | 152.6 | tg-6291758717884957491 |
| 24 | ❤️ | image/png | 246x256 | 240.2 | tg-6291644892661678941 |
| 25 | ❤️ | image/png | 242x256 | 250.3 | tg-6291891690072441710 |
| 26 | ❤️ | image/png | 238x256 | 263.3 | tg-6291612731946566256 |
| 27 | ❤️ | image/png | 256x256 | 279.9 | tg-6321151571388269330 |
| 28 | ❤️ | image/png | 256x248 | 242.5 | tg-6323074222088258964 |
| 29 | ❤️ | image/png | 196x256 | 257.4 | tg-6325802346659971879 |
| 30 | ❤️ | image/png | 256x246 | 236.4 | tg-6327847171999663227 |
| 31 | ❤️ | image/png | 216x256 | 230.6 | tg-6334421830626968367 |
| 32 | ❤️ | image/png | 224x256 | 223.5 | tg-6332390624628573312 |
| 33 | ❤️ | image/png | 254x256 | 255.7 | tg-6053130961984422736 |
| 34 | ❤️ | image/png | 256x256 | 301.3 | tg-6055460307432637362 |
| 35 | ❤️ | image/png | 256x200 | 217.8 | tg-6089326077316957540 |
| 36 | ❤️ | image/png | 244x256 | 272.1 | tg-6109618367566447494 |
| 37 | ❤️ | image/png | 256x191 | 196.5 | tg-6107409444411278077 |
| 38 | ❤️ | image/png | 256x255 | 263.7 | tg-6107021157892883443 |
| 39 | ❤️ | image/png | 256x226 | 221.1 | tg-6172577313905968423 |
| 40 | ❤️ | image/png | 256x256 | 565.0 | tg-6170478921734161474 |
| 41 | ❤️ | image/png | 256x227 | 263.7 | tg-6172282868128023871 |


## 43. `自用` — `realYoshino.json`

- 標題:`自用`;包 ID:`tg-4253476503162978303`
- 張數:61;mimetype 分佈:image/png ×61
- 大小統計:合計 15,426,916 B(14.71 MB);平均 247.0 KB;最小 137.8 KB;最大 477.9 KB
- 來源 ID:tg- ×61

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 😱 | image/png | 256x215 | 310.0 | tg-6149841483617797749 |
| 2 | 😋 | image/png | 256x255 | 261.7 | tg-6152032041492809197 |
| 3 | 😊 | image/png | 255x256 | 402.7 | tg-6158824725544961744 |
| 4 | 😇 | image/png | 256x246 | 204.4 | tg-6168181784245700845 |
| 5 | 😋 | image/png | 256x231 | 424.3 | tg-6174985545018509336 |
| 6 | 😇 | image/png | 253x256 | 261.1 | tg-6186072165574509862 |
| 7 | 😋 | image/png | 256x256 | 316.8 | tg-6197310621814360211 |
| 8 | 😇 | image/png | 148x256 | 208.7 | tg-6201999935827609087 |
| 9 | 😃 | image/png | 256x176 | 291.9 | tg-6203995463532677929 |
| 10 | 😝 | image/png | 253x256 | 216.0 | tg-6217749696866158042 |
| 11 | 🤤 | image/png | 221x256 | 238.1 | tg-6217316579479127798 |
| 12 | 😋 | image/png | 235x256 | 332.0 | tg-6224502205794224127 |
| 13 | 😋 | image/png | 256x216 | 304.6 | tg-6224252337481844104 |
| 14 | 😱 | image/png | 256x256 | 251.6 | tg-6224285245521266390 |
| 15 | 😱 | image/png | 256x194 | 189.8 | tg-6228507172603430956 |
| 16 | 😕 | image/png | 164x256 | 187.5 | tg-6228907652533978965 |
| 17 | 😢 | image/png | 256x192 | 351.5 | tg-6233508047839299538 |
| 18 | 😏 | image/png | 256x223 | 174.5 | tg-6237700979597248193 |
| 19 | 😏 | image/png | 256x200 | 137.8 | tg-6237753219284470741 |
| 20 | 😏 | image/png | 239x256 | 231.5 | tg-6255588023736469059 |
| 21 | 🥵 | image/png | 256x256 | 220.9 | tg-6264958225037133650 |
| 22 | 😇 | image/png | 256x238 | 477.9 | tg-6266984045146539717 |
| 23 | 😋 | image/png | 256x256 | 365.9 | tg-6269302056176060108 |
| 24 | 👋 | image/png | 256x256 | 307.9 | tg-6267275372778227691 |
| 25 | 🤪 | image/png | 256x256 | 224.0 | tg-6273890713335761468 |
| 26 | 😭 | image/png | 256x140 | 142.7 | tg-6276189375537612661 |
| 27 | 😖 | image/png | 222x256 | 188.4 | tg-6278551972622633018 |
| 28 | 😕 | image/png | 256x256 | 168.1 | tg-6280447818431727565 |
| 29 | 😕 | image/png | 256x245 | 210.0 | tg-6287408740647831732 |
| 30 | 😕 | image/png | 199x256 | 167.7 | tg-6287032965369169537 |
| 31 | 😔 | image/png | 256x186 | 170.5 | tg-6291814251812095766 |
| 32 | 😏 | image/png | 256x241 | 203.9 | tg-6302922153931049164 |
| 33 | 😔 | image/png | 256x239 | 200.5 | tg-6316821089007699870 |
| 34 | 😇 | image/png | 256x256 | 219.9 | tg-6318678679543088934 |
| 35 | 😱 | image/png | 256x256 | 207.7 | tg-6332138449918757278 |
| 36 | 🥬 | image/png | 256x256 | 230.5 | tg-6055560633573705876 |
| 37 | 😋 | image/png | 256x256 | 337.8 | tg-6073487436225185474 |
| 38 | 😕 | image/png | 256x256 | 305.6 | tg-6210933459213355276 |
| 39 | 😋 | image/png | 247x256 | 285.7 | tg-6267307743946738264 |
| 40 | 😱 | image/png | 256x159 | 167.9 | tg-6316687519819761812 |
| 41 | 😭 | image/png | 256x149 | 138.7 | tg-6055564834051722719 |
| 42 | 😋 | image/png | 216x256 | 233.9 | tg-6147936463758560170 |
| 43 | 😢 | image/png | 214x256 | 224.5 | tg-6149806737332374583 |
| 44 | 😢 | image/png | 192x256 | 166.8 | tg-6163527650309573749 |
| 45 | 😋 | image/png | 256x243 | 226.2 | tg-6269232370331684477 |
| 46 | 😆 | image/png | 256x232 | 234.4 | tg-6269367017556413243 |
| 47 | 😋 | image/png | 233x256 | 213.7 | tg-6267049410253819796 |
| 48 | 😝 | image/png | 256x256 | 248.5 | tg-6280570379618488254 |
| 49 | 😋 | image/png | 256x256 | 327.0 | tg-6285222022473584045 |
| 50 | 😵 | image/png | 217x256 | 222.9 | tg-6325550116115582401 |
| 51 | 😇 | image/png | 256x256 | 343.6 | tg-6055233215331830954 |
| 52 | 😋 | image/png | 256x192 | 239.4 | tg-6091660546661158389 |
| 53 | 😋 | image/png | 167x256 | 221.6 | tg-6131910282919807999 |
| 54 | 😋 | image/png | 254x256 | 296.2 | tg-6159068739816918465 |
| 55 | 😋 | image/png | 241x256 | 230.0 | tg-6158993921486622133 |
| 56 | 😋 | image/png | 256x224 | 272.7 | tg-6170340705391611214 |
| 57 | 😋 | image/png | 256x256 | 219.2 | tg-6222090182225563870 |
| 58 | 😋 | image/png | 256x241 | 203.4 | tg-6237742593535381250 |
| 59 | 😋 | image/png | 256x174 | 192.4 | tg-6242250685698543040 |
| 60 | 😋 | image/png | 256x192 | 281.3 | tg-6091318302192177049 |
| 61 | 😇 | image/png | 256x256 | 229.0 | tg-6219505488086702113 |


## 44. `𝔸𝕫𝕦𝕟𝕖𝕜𝕠` — `inekokkk_by_fStikBot.json`

- 標題:`𝔸𝕫𝕦𝕟𝕖𝕜𝕠`;包 ID:`tg-970173987634020349`
- 張數:120;mimetype 分佈:image/png ×98;video/webm ×19;image/gif ×3
- 大小統計:合計 22,302,725 B(21.27 MB);平均 181.5 KB;最小 18.9 KB;最大 417.5 KB
- 來源 ID:tg- ×120

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🥵 | image/png | 256x256 | 160.0 | tg-6336928888936992520 |
| 2 | 👙 | image/png | 256x256 | 148.1 | tg-6336681335611985510 |
| 3 | 🛏 | image/png | 256x256 | 166.5 | tg-6334427272350535796 |
| 4 | 😐 | image/png | 198x256 | 113.6 | tg-6334455679264231554 |
| 5 | 👀 | image/png | 256x234 | 215.0 | tg-6334329656333832610 |
| 6 | 🎱 | video/webm | 512x512 | 251.3 | tg-6334552406222704850 |
| 7 | 🌟 | video/webm | 510x512 | 32.9 | tg-6334530347270672121 |
| 8 | 🌟 | video/webm | 502x512 | 23.5 | tg-6336753705810923473 |
| 9 | 😚 | image/png | 256x256 | 261.6 | tg-6336589672419954214 |
| 10 | ☺ | image/png | 256x256 | 172.5 | tg-6334379671227995845 |
| 11 | 😐 | image/png | 256x256 | 141.8 | tg-6334535140454175276 |
| 12 | 🥰 | image/png | 256x256 | 175.0 | tg-6336688753020506260 |
| 13 | 🥰 | image/png | 256x256 | 193.2 | tg-6336923000536830683 |
| 14 | 😠 | image/png | 256x256 | 155.5 | tg-6336593851423133012 |
| 15 | 😂 | image/png | 256x242 | 236.8 | tg-6337077692373930459 |
| 16 | 😃 | image/png | 256x251 | 194.5 | tg-6336748156713177028 |
| 17 | 😝 | video/webm | 512x512 | 84.6 | tg-6334421882166580187 |
| 18 | 👀 | image/png | 256x248 | 168.9 | tg-6334635509544915838 |
| 19 | 🤡 | image/png | 256x253 | 227.5 | tg-6334821752211772250 |
| 20 | 😶 | image/png | 256x134 | 64.3 | tg-6336735469379784653 |
| 21 | 🐱 | image/png | 256x256 | 289.1 | tg-6336668111407681758 |
| 22 | ✨ | image/png | 256x157 | 92.6 | tg-6337007044456878647 |
| 23 | ✨ | image/png | 256x155 | 91.5 | tg-6337016179852316730 |
| 24 | 👇 | video/webm | 512x512 | 159.4 | tg-6336826514096525210 |
| 25 | 👀 | video/webm | 512x512 | 111.8 | tg-6336911915226238986 |
| 26 | 🏃‍♀ | video/webm | 512x508 | 194.0 | tg-6336807062189641650 |
| 27 | 😮 | video/webm | 512x512 | 33.0 | tg-6336969300284280944 |
| 28 | 😎 | image/png | 256x144 | 163.7 | tg-6337099661131649001 |
| 29 | 😃 | image/png | 256x256 | 100.1 | tg-6337059979928800927 |
| 30 | ❤ | image/png | 256x256 | 328.5 | tg-6336732321168757649 |
| 31 | ☺ | image/png | 252x256 | 222.2 | tg-6336917803626402032 |
| 32 | 😏 | image/png | 195x256 | 153.5 | tg-6334769628488667532 |
| 33 | 😃 | image/png | 256x249 | 141.8 | tg-6339267657543454424 |
| 34 | 😀 | image/png | 256x256 | 182.2 | tg-6339139826431823273 |
| 35 | 👀 | image/png | 192x256 | 283.5 | tg-6338958011876249641 |
| 36 | 😀 | image/png | 256x202 | 262.7 | tg-6336980140781735878 |
| 37 | 😑 | image/png | 256x132 | 58.4 | tg-6336772126925656203 |
| 38 | 🏆 | image/png | 256x240 | 211.9 | tg-6338888609499714829 |
| 39 | 🐟 | image/png | 256x240 | 182.8 | tg-6336957849901469924 |
| 40 | 😣 | image/png | 256x212 | 169.8 | tg-6339199595196715320 |
| 41 | 🖊 | image/png | 256x256 | 339.3 | tg-6336829271465528884 |
| 42 | 🤬 | video/webm | 410x512 | 135.8 | tg-6336839459127954851 |
| 43 | 🎆 | image/png | 256x256 | 157.2 | tg-6339028423570100182 |
| 44 | 😢 | image/png | 256x195 | 162.0 | tg-6336913341155380924 |
| 45 | 🚮 | image/png | 256x256 | 206.3 | tg-6336796200217350019 |
| 46 | ❤ | image/png | 256x212 | 236.9 | tg-6339311895706603177 |
| 47 | 🚛 | image/png | 194x256 | 216.9 | tg-6339138224409022482 |
| 48 | 💣 | image/png | 256x192 | 168.7 | tg-6337069544820969582 |
| 49 | 👀 | image/png | 256x202 | 116.6 | tg-6339373378163446822 |
| 50 | 📎 | image/png | 256x256 | 184.5 | tg-6339135741917926274 |
| 51 | 🤲 | image/png | 256x256 | 148.4 | tg-6339326713343775273 |
| 52 | 🔳 | image/png | 256x256 | 297.7 | tg-6336854963959894298 |
| 53 | ✋ | image/png | 256x256 | 215.8 | tg-6336882881247317852 |
| 54 | 👄 | image/png | 256x256 | 148.6 | tg-6339210092096786338 |
| 55 | 👄 | image/png | 256x256 | 159.1 | tg-6339165591940632636 |
| 56 | 🖼 | image/png | 256x256 | 134.6 | tg-6339215112913555480 |
| 57 | 😅 | image/png | 256x256 | 196.0 | tg-6339197555087249793 |
| 58 | 🌟 | image/png | 256x256 | 199.0 | tg-6053023050931114008 |
| 59 | 😏 | image/png | 248x256 | 110.6 | tg-6053385005005017790 |
| 60 | 😒 | image/png | 256x244 | 205.4 | tg-6052842520570761235 |
| 61 | 🤭 | image/png | 256x249 | 148.8 | tg-6052869067763618252 |
| 62 | 😢 | image/png | 238x256 | 170.8 | tg-6053387736604217365 |
| 63 | 🥵 | image/png | 256x232 | 240.5 | tg-6053193595492503785 |
| 64 | 😯 | image/png | 253x256 | 302.7 | tg-6053341789044085434 |
| 65 | 😡 | image/png | 256x256 | 147.2 | tg-6062103926054851098 |
| 66 | ⭐ | video/webm | 512x503 | 23.7 | tg-6066635777977094225 |
| 67 | 😃 | image/png | 246x256 | 213.5 | tg-6066465044437143630 |
| 68 | 🌟 | image/png | 256x256 | 283.0 | tg-6075841898642148376 |
| 69 | 🐔 | image/png | 256x256 | 363.3 | tg-6087006666128101133 |
| 70 | 🍳 | video/webm | 512x512 | 189.9 | tg-6089088054524383019 |
| 71 | 🌟 | video/webm | 512x512 | 20.4 | tg-6088901859102166766 |
| 72 | 😀 | image/png | 218x256 | 130.6 | tg-6100523950410830606 |
| 73 | 💖 | image/png | 256x221 | 170.1 | tg-6102535541293584147 |
| 74 | 🥵 | image/png | 256x256 | 233.1 | tg-6100392816469348465 |
| 75 | 😶 | image/png | 256x240 | 236.9 | tg-6100262945248252382 |
| 76 | 😂 | video/webm | 512x512 | 196.8 | tg-6147651527038210372 |
| 77 | 🌟 | image/png | 256x256 | 202.2 | tg-6147710179111604253 |
| 78 | 🫰 | image/png | 256x256 | 352.0 | tg-6147646231343534850 |
| 79 | 🤐 | image/png | 256x210 | 367.4 | tg-6147739256040198985 |
| 80 | ⭐ | image/png | 256x214 | 175.8 | tg-6228858758626284206 |
| 81 | ⭐ | image/png | 256x213 | 165.1 | tg-6228980134402068908 |
| 82 | ⭐ | image/png | 256x221 | 165.7 | tg-6230731746619429295 |
| 83 | ⭐ | image/png | 256x221 | 162.3 | tg-6230885686837252278 |
| 84 | ⭐ | image/png | 256x200 | 126.4 | tg-6228984360649888280 |
| 85 | ⭐ | image/png | 256x246 | 183.2 | tg-6231038991399916156 |
| 86 | ⭐ | image/png | 256x225 | 165.5 | tg-6228695167616947045 |
| 87 | ⭐ | image/png | 243x256 | 170.6 | tg-6228924377136632856 |
| 88 | ⭐ | image/png | 256x224 | 206.0 | tg-6228521461959627510 |
| 89 | ⭐ | image/png | 256x251 | 203.1 | tg-6228679336367493491 |
| 90 | ⭐ | image/png | 256x211 | 184.0 | tg-6228915134367010557 |
| 91 | ⭐ | image/png | 214x256 | 170.8 | tg-6228868151719760470 |
| 92 | 😦 | image/gif | 256x256 | 207.2 | tg-6230965440084972066 |
| 93 | 😱 | image/gif | 256x256 | 228.0 | tg-6228823707398181295 |
| 94 | 😤 | image/gif | 256x256 | 127.7 | tg-6066364452008104817 |
| 95 | ⭐ | video/webm | 512x480 | 18.9 | tg-6093709246061352593 |
| 96 | 😢 | image/png | 256x256 | 147.0 | tg-6230989925693526504 |
| 97 | ❤ | image/png | 205x256 | 254.7 | tg-6289611375970882268 |
| 98 | ❤ | image/png | 145x256 | 155.0 | tg-6289747109822337415 |
| 99 | 🌟 | video/webm | 512x489 | 125.0 | tg-6298507451536773494 |
| 100 | 🙃 | image/png | 185x256 | 256.6 | tg-6298505879578743804 |
| 101 | 😅 | image/png | 256x203 | 175.5 | tg-6298530485446382619 |
| 102 | 😍 | video/webm | 512x358 | 174.9 | tg-6302981738012348742 |
| 103 | 🚬 | video/webm | 512x495 | 106.2 | tg-6064280989142619113 |
| 104 | 🚿 | image/png | 192x256 | 223.6 | tg-6095875541666107939 |
| 105 | 😀 | video/webm | 218x512 | 62.1 | tg-6093733551281280480 |
| 106 | 🥬 | image/png | 256x254 | 302.0 | tg-6240222494767191349 |
| 107 | 🤣 | image/png | 256x256 | 166.4 | tg-6251196973727093645 |
| 108 | 😡 | image/png | 256x256 | 201.7 | tg-6273616045882217541 |
| 109 | 👄 | image/png | 256x256 | 156.1 | tg-6273649778555360418 |
| 110 | 😁 | image/png | 256x256 | 175.3 | tg-6273634475586885625 |
| 111 | 🫥 | image/png | 256x256 | 417.5 | tg-6066809642548204893 |
| 112 | 👍 | image/png | 256x256 | 340.9 | tg-6091311971410383984 |
| 113 | 👍 | image/png | 256x256 | 218.2 | tg-6093920657236562946 |
| 114 | 👍 | image/png | 256x256 | 212.5 | tg-6111746227508876341 |
| 115 | 🌟 | video/webm | 506x512 | 57.8 | tg-6145212664218915543 |
| 116 | 🌚 | image/png | 256x180 | 102.3 | tg-6143326331762382158 |
| 117 | 🌟 | image/png | 232x256 | 157.0 | tg-6159031897587455544 |
| 118 | 🙈 | image/png | 256x254 | 187.2 | tg-6233504251088213531 |
| 119 | 🫥 | image/png | 256x256 | 348.2 | tg-6267149916783515839 |
| 120 | 👩‍🤝‍👨 | image/png | 256x102 | 44.4 | tg-6165553603562968900 |


## 45. `ラブライブ！にじよん @moe_sticker_bot @Takius` — `line_220157684395_by_moe_sticker_bot.json`

- 標題:`ラブライブ！にじよん @moe_sticker_bot @Takius`;包 ID:`tg-187010637073743884`
- 張數:40;mimetype 分佈:image/png ×40
- 大小統計:合計 9,355,852 B(8.92 MB);平均 228.4 KB;最小 157.9 KB;最大 320.6 KB
- 來源 ID:tg- ×40

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 👋 | image/png | 256x221 | 207.5 | tg-6255693765831296580 |
| 2 | ⁉️ | image/png | 256x221 | 183.5 | tg-6255819402214639589 |
| 3 | 😣 | image/png | 256x221 | 208.5 | tg-6256052464319990347 |
| 4 | ☺️ | image/png | 256x221 | 185.7 | tg-6255602489186322672 |
| 5 | 😈 | image/png | 256x221 | 184.1 | tg-6255894181890230150 |
| 6 | 😭 | image/png | 256x221 | 174.3 | tg-6255729418354821003 |
| 7 | 🥰 | image/png | 256x221 | 213.3 | tg-6255614223036975229 |
| 8 | 😳 | image/png | 256x221 | 224.2 | tg-6253389795049867337 |
| 9 | 🗣 | image/png | 256x221 | 268.2 | tg-6255943213236881804 |
| 10 | 💕 | image/png | 256x221 | 229.0 | tg-6255862424902043944 |
| 11 | 🤭 | image/png | 256x221 | 209.2 | tg-6255713415306676321 |
| 12 | 😋 | image/png | 256x221 | 177.0 | tg-6255752267580835471 |
| 13 | 🖖 | image/png | 256x221 | 217.7 | tg-6255933515200726657 |
| 14 | 🙇‍♀️ | image/png | 256x221 | 221.6 | tg-6255640460992186289 |
| 15 | 😆 | image/png | 256x221 | 252.4 | tg-6255790922286499395 |
| 16 | 🤩 | image/png | 256x221 | 277.9 | tg-6256046915222243033 |
| 17 | 🤗 | image/png | 256x221 | 218.2 | tg-6255803562375252238 |
| 18 | 😴 | image/png | 256x221 | 188.6 | tg-6255502532412442713 |
| 19 | 😆 | image/png | 256x221 | 301.1 | tg-6255567657001551673 |
| 20 | 🆗 | image/png | 256x221 | 275.2 | tg-6255573188919428948 |
| 21 | 📷 | image/png | 256x221 | 258.3 | tg-6255862738434656023 |
| 22 | 🤤 | image/png | 256x221 | 240.4 | tg-6253499467039770712 |
| 23 | 💁‍♀️ | image/png | 256x221 | 233.1 | tg-6255906993777673878 |
| 24 | 😉 | image/png | 256x221 | 228.9 | tg-6255842169836275575 |
| 25 | 🥳 | image/png | 256x221 | 290.2 | tg-6255779656587282055 |
| 26 | 😨 | image/png | 256x221 | 183.1 | tg-6255752057127438224 |
| 27 | ㊗️ | image/png | 256x221 | 241.8 | tg-6255822692159588381 |
| 28 | 🤔 | image/png | 256x221 | 157.9 | tg-6253542678705736497 |
| 29 | 😺 | image/png | 256x221 | 205.4 | tg-6256008651358603854 |
| 30 | 😅 | image/png | 256x221 | 187.6 | tg-6253455387790411810 |
| 31 | 😮‍💨 | image/png | 256x221 | 171.4 | tg-6255879763685017570 |
| 32 | 🧐 | image/png | 256x221 | 180.8 | tg-6255718418943575619 |
| 33 | 😀 | image/png | 256x221 | 186.5 | tg-6255707591331022568 |
| 34 | 🙂 | image/png | 256x221 | 269.0 | tg-6255850867145050083 |
| 35 | 💯 | image/png | 256x221 | 260.3 | tg-6255839863438837323 |
| 36 | 🫂 | image/png | 256x221 | 277.0 | tg-6255620609653344191 |
| 37 | 🉑 | image/png | 256x221 | 317.9 | tg-6253790064527017971 |
| 38 | 💮 | image/png | 256x221 | 223.1 | tg-6256047855820081585 |
| 39 | 💤 | image/png | 256x221 | 320.6 | tg-6255757666354726482 |
| 40 | 😭 | image/png | 256x221 | 286.1 | tg-6255889212613069705 |


## 46. `滥权` — `WikiAbusers.json`

- 標題:`滥权`;包 ID:`tg-548635020697272321`
- 張數:120;mimetype 分佈:image/png ×120
- 大小統計:合計 16,413,321 B(15.65 MB);平均 133.6 KB;最小 4.5 KB;最大 272.8 KB
- 來源 ID:tg- ×120

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🦆 | image/png | 256x132 | 49.1 | tg-548635020697272339 |
| 2 | 😕 | image/png | 256x256 | 140.9 | tg-548635020697272371 |
| 3 | 😒 | image/png | 256x65 | 44.4 | tg-548635020697272338 |
| 4 | ⬆ | image/png | 256x132 | 7.7 | tg-548635020697272340 |
| 5 | ⬇ | image/png | 256x132 | 7.2 | tg-548635020697272341 |
| 6 | ↕ | image/png | 256x132 | 12.1 | tg-548635020697272342 |
| 7 | 😒 | image/png | 256x132 | 22.7 | tg-548635020697272343 |
| 8 | 💔 | image/png | 256x178 | 49.3 | tg-548635020697272345 |
| 9 | 💔 | image/png | 256x178 | 48.1 | tg-548635020697272346 |
| 10 | 😾 | image/png | 256x178 | 48.2 | tg-548635020697272347 |
| 11 | 🔰 | image/png | 256x178 | 34.8 | tg-548635020697272348 |
| 12 | 🤖 | image/png | 256x256 | 114.1 | tg-548635020697272349 |
| 13 | 🎉 | image/png | 256x256 | 235.7 | tg-548635020697272350 |
| 14 | 🕵 | image/png | 256x256 | 167.9 | tg-548635020697272351 |
| 15 | 😏 | image/png | 256x256 | 165.0 | tg-548635020697272392 |
| 16 | 🕵 | image/png | 256x256 | 91.0 | tg-548635020697272372 |
| 17 | 🛡 | image/png | 256x256 | 83.6 | tg-548635020697272353 |
| 18 | ↪ | image/png | 256x256 | 101.3 | tg-548635020697272354 |
| 19 | 👆 | image/png | 256x256 | 24.4 | tg-548635020697272356 |
| 20 | 💪 | image/png | 256x256 | 142.5 | tg-548635020697272357 |
| 21 | 😏 | image/png | 256x256 | 149.9 | tg-548635020697272358 |
| 22 | 📈 | image/png | 256x256 | 209.2 | tg-548635020697272360 |
| 23 | ❌ | image/png | 256x101 | 43.2 | tg-548635020697272361 |
| 24 | 😈 | image/png | 256x165 | 113.7 | tg-548635020697272362 |
| 25 | 🔫 | image/png | 256x188 | 78.7 | tg-548635020697272373 |
| 26 | 🔪 | image/png | 256x251 | 133.4 | tg-548635020697272363 |
| 27 | 🙇 | image/png | 256x256 | 202.6 | tg-548635020697272365 |
| 28 | 🤖 | image/png | 256x230 | 233.9 | tg-548635020697272377 |
| 29 | 💁 | image/png | 256x256 | 134.0 | tg-548635020697272378 |
| 30 | 💁 | image/png | 256x256 | 221.7 | tg-548635020697272366 |
| 31 | 👧 | image/png | 256x256 | 272.8 | tg-548635020697272367 |
| 32 | 😈 | image/png | 256x256 | 188.9 | tg-548635020697272370 |
| 33 | 🙏 | image/png | 256x112 | 40.2 | tg-548635020697272369 |
| 34 | 😒 | image/png | 256x256 | 140.9 | tg-548635020697272374 |
| 35 | 😒 | image/png | 256x256 | 137.4 | tg-548635020697272375 |
| 36 | 🔪 | image/png | 256x256 | 165.2 | tg-548635020697272379 |
| 37 | 👬 | image/png | 256x256 | 130.4 | tg-548635020697272380 |
| 38 | 👊 | image/png | 256x256 | 135.4 | tg-548635020697272381 |
| 39 | 😭 | image/png | 256x256 | 184.8 | tg-548635020697272382 |
| 40 | 😶 | image/png | 256x256 | 85.7 | tg-548635020697272383 |
| 41 | 🔰 | image/png | 256x256 | 83.5 | tg-548635020697272384 |
| 42 | 🚬 | image/png | 256x256 | 112.9 | tg-548635020697272385 |
| 43 | 💬 | image/png | 256x256 | 221.0 | tg-548635020697272386 |
| 44 | 💬 | image/png | 256x256 | 214.5 | tg-548635020697272413 |
| 45 | 💬 | image/png | 256x256 | 213.9 | tg-548635020697272414 |
| 46 | 💬 | image/png | 256x256 | 229.1 | tg-548635020697272437 |
| 47 | 💬 | image/png | 256x256 | 238.6 | tg-548635020697272436 |
| 48 | 🔪 | image/png | 256x256 | 162.9 | tg-548635020697272387 |
| 49 | 🎤 | image/png | 256x256 | 118.8 | tg-548635020697272388 |
| 50 | 🤔 | image/png | 256x256 | 210.9 | tg-548635020697272389 |
| 51 | 🖕 | image/png | 256x256 | 187.7 | tg-548635020697272390 |
| 52 | 😏 | image/png | 256x256 | 264.1 | tg-548635020697272391 |
| 53 | 🤦 | image/png | 256x256 | 162.4 | tg-548635020697272393 |
| 54 | 🙃 | image/png | 256x256 | 152.0 | tg-548635020697272394 |
| 55 | 🙃 | image/png | 256x256 | 119.9 | tg-548635020697272397 |
| 56 | 😏 | image/png | 256x256 | 151.2 | tg-548635020697272399 |
| 57 | 😈 | image/png | 256x256 | 158.8 | tg-548635020697272401 |
| 58 | 😤 | image/png | 256x256 | 181.6 | tg-548635020697272402 |
| 59 | 👨‍💻 | image/png | 256x256 | 120.2 | tg-548635020697272403 |
| 60 | 💋 | image/png | 256x256 | 223.3 | tg-548635020697272404 |
| 61 | 😒 | image/png | 256x256 | 168.2 | tg-548635020697272406 |
| 62 | 🔫 | image/png | 256x256 | 132.0 | tg-548635020697272359 |
| 63 | 😏 | image/png | 256x256 | 103.8 | tg-548635020697272376 |
| 64 | 😏 | image/png | 256x256 | 158.9 | tg-548635020697272407 |
| 65 | 🤦‍♀️ | image/png | 256x256 | 145.4 | tg-548635020697272409 |
| 66 | 👊 | image/png | 256x256 | 149.5 | tg-548635020697272410 |
| 67 | 🍗 | image/png | 256x256 | 149.8 | tg-548635020697272411 |
| 68 | 👊 | image/png | 256x256 | 153.0 | tg-548635020697272412 |
| 69 | 👊 | image/png | 256x256 | 158.4 | tg-548635020697272421 |
| 70 | 🚫 | image/png | 256x100 | 58.6 | tg-548635020697272415 |
| 71 | 💁 | image/png | 256x256 | 112.9 | tg-548635020697272416 |
| 72 | 👮 | image/png | 256x256 | 162.2 | tg-548635020697272420 |
| 73 | 🥟 | image/png | 256x256 | 10.4 | tg-548635020697272422 |
| 74 | 🔫 | image/png | 256x256 | 166.3 | tg-548635020697272423 |
| 75 | 👏 | image/png | 256x256 | 68.6 | tg-548635020697272426 |
| 76 | 👮‍♀️ | image/png | 256x256 | 204.8 | tg-548635020697272427 |
| 77 | 👆 | image/png | 256x256 | 163.0 | tg-548635020697272428 |
| 78 | 📲 | image/png | 256x256 | 125.2 | tg-548635020697272429 |
| 79 | 😂 | image/png | 256x256 | 190.0 | tg-548635020697272431 |
| 80 | 😭 | image/png | 256x256 | 192.0 | tg-548635020697272432 |
| 81 | 🈲 | image/png | 223x256 | 96.4 | tg-548635020697272433 |
| 82 | 😤 | image/png | 256x256 | 190.8 | tg-548635020697272434 |
| 83 | 😈 | image/png | 256x256 | 204.3 | tg-548635020697272435 |
| 84 | ✅ | image/png | 256x256 | 44.9 | tg-548635020697272438 |
| 85 | 🤷‍♀️ | image/png | 256x256 | 130.6 | tg-548635020697272439 |
| 86 | 👨‍❤️‍👨 | image/png | 256x256 | 151.2 | tg-548635020697272440 |
| 87 | 💂‍♀️ | image/png | 256x256 | 117.0 | tg-548635020697272441 |
| 88 | 👩‍💻 | image/png | 256x256 | 152.5 | tg-548635020697272443 |
| 89 | 🕵️ | image/png | 256x256 | 157.0 | tg-548635020697272444 |
| 90 | 🔥 | image/png | 256x256 | 202.2 | tg-548635020697272445 |
| 91 | 👋 | image/png | 256x256 | 115.0 | tg-548635020697272446 |
| 92 | 👩‍💻 | image/png | 256x256 | 113.8 | tg-548635020697272447 |
| 93 | 👨‍💻 | image/png | 256x256 | 113.9 | tg-548635020697272448 |
| 94 | 👩‍💻 | image/png | 256x256 | 134.6 | tg-548635020697272449 |
| 95 | 😈 | image/png | 256x256 | 166.6 | tg-548635020697272450 |
| 96 | ⚠️ | image/png | 256x256 | 130.8 | tg-548635020697272451 |
| 97 | 😾 | image/png | 256x256 | 128.2 | tg-548635020697272452 |
| 98 | ✏️ | image/png | 256x256 | 194.1 | tg-548635020697272453 |
| 99 | ✏️ | image/png | 256x256 | 160.4 | tg-548635020697272454 |
| 100 | 👩‍💻 | image/png | 256x256 | 119.8 | tg-548635020697272455 |
| 101 | 🥟 | image/png | 256x102 | 52.5 | tg-548635020697272459 |
| 102 | 🙇‍♀️ | image/png | 256x256 | 94.2 | tg-548635020697272460 |
| 103 | 🙅 | image/png | 256x256 | 4.5 | tg-548635020697272461 |
| 104 | ☠️ | image/png | 256x256 | 158.9 | tg-548635020697272462 |
| 105 | 😈 | image/png | 256x256 | 144.1 | tg-548635020697272463 |
| 106 | 🤷‍♀️ | image/png | 256x256 | 121.3 | tg-548635020697272464 |
| 107 | 👆 | image/png | 256x256 | 86.0 | tg-548635020697272466 |
| 108 | 🙄 | image/png | 256x206 | 86.2 | tg-548635020697272468 |
| 109 | 🙄 | image/png | 256x206 | 85.1 | tg-548635020697272469 |
| 110 | 💁 | image/png | 212x256 | 176.5 | tg-548635020697272470 |
| 111 | 😭 | image/png | 256x256 | 182.5 | tg-548635020697272471 |
| 112 | 😭 | image/png | 256x256 | 182.3 | tg-548635020697272472 |
| 113 | 😓 | image/png | 256x256 | 163.8 | tg-548635020697272473 |
| 114 | 😅 | image/png | 256x256 | 122.0 | tg-548635020697272474 |
| 115 | 📼 | image/png | 256x256 | 83.2 | tg-548635020697272475 |
| 116 | 🙂 | image/png | 256x42 | 9.3 | tg-548635020697272476 |
| 117 | 🙃 | image/png | 256x42 | 9.3 | tg-548635020697272477 |
| 118 | ⬆️ | image/png | 256x256 | 103.4 | tg-548635020697272478 |
| 119 | 👊 | image/png | 256x256 | 213.5 | tg-548635020697272479 |
| 120 | 💰 | image/png | 256x256 | 234.3 | tg-548635020697272480 |


## 47. `流萤小表情 | Pixiv: ek121` — `firefly_ek121_1_by_moe_sticker_bot.json`

- 標題:`流萤小表情 | Pixiv: ek121`;包 ID:`tg-4901800072745844755`
- 張數:69;mimetype 分佈:image/png ×69
- 大小統計:合計 18,822,814 B(17.95 MB);平均 266.4 KB;最小 98.9 KB;最大 392.9 KB
- 來源 ID:tg- ×69

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | ❤️ | image/png | 256x189 | 249.4 | tg-6285253826706411879 |
| 2 | 😣 | image/png | 256x256 | 334.0 | tg-6285055412102238683 |
| 3 | 😄 | image/png | 256x256 | 334.1 | tg-6284872691308564467 |
| 4 | 😠 | image/png | 256x256 | 327.3 | tg-6285166488546447784 |
| 5 | 🥰 | image/png | 256x256 | 332.0 | tg-6284982603816636552 |
| 6 | 😡 | image/png | 256x256 | 328.7 | tg-6285025982986326458 |
| 7 | 🤗 | image/png | 256x256 | 336.2 | tg-6284885941282672258 |
| 8 | ❓ | image/png | 256x256 | 332.6 | tg-6285151640844505671 |
| 9 | 💴 | image/png | 256x256 | 320.6 | tg-6285086469010756135 |
| 10 | 🤗 | image/png | 256x256 | 338.0 | tg-6285007110900027119 |
| 11 | 😉 | image/png | 256x174 | 214.3 | tg-6282945900260101893 |
| 12 | 🔥 | image/png | 256x256 | 259.0 | tg-6285231282423074710 |
| 13 | 🔥 | image/png | 256x256 | 306.4 | tg-6285186434374569904 |
| 14 | 🔥 | image/png | 256x256 | 336.2 | tg-6285298313977663952 |
| 15 | 🔥 | image/png | 256x256 | 317.5 | tg-6284884837476078558 |
| 16 | 🔥 | image/png | 256x256 | 392.1 | tg-6284816225373524402 |
| 17 | 🔥 | image/png | 256x256 | 392.9 | tg-6285305804400627424 |
| 18 | 🔥 | image/png | 256x256 | 98.9 | tg-6284880727192375240 |
| 19 | 🔥 | image/png | 256x256 | 124.6 | tg-6282705317667016919 |
| 20 | 🔥 | image/png | 256x256 | 278.0 | tg-6282554169177935900 |
| 21 | 😮‍💨 | image/png | 256x207 | 242.2 | tg-6284778816208375665 |
| 22 | 😆 | image/png | 256x256 | 203.2 | tg-6284959776065458411 |
| 23 | 😮‍💨 | image/png | 256x256 | 250.8 | tg-6284950030784665142 |
| 24 | 🙂 | image/png | 256x150 | 178.0 | tg-6285162043255297015 |
| 25 | 😕 | image/png | 256x256 | 242.0 | tg-6285040237982781081 |
| 26 | 😣 | image/png | 256x256 | 224.0 | tg-6284916710428380751 |
| 27 | 😟 | image/png | 256x256 | 304.0 | tg-6285091360978506073 |
| 28 | 🚀 | image/png | 256x256 | 319.5 | tg-6285228615248384073 |
| 29 | 😫 | image/png | 256x256 | 238.0 | tg-6285126609775104454 |
| 30 | 😳 | image/png | 256x256 | 252.6 | tg-6285205375180345651 |
| 31 | 😀 | image/png | 256x191 | 196.0 | tg-6285077535478779947 |
| 32 | 😔 | image/png | 256x191 | 189.6 | tg-6284973056104337628 |
| 33 | 😃 | image/png | 256x191 | 209.0 | tg-6285049115680182466 |
| 34 | 🥰 | image/png | 256x256 | 231.3 | tg-6284918329631052194 |
| 35 | 🥲 | image/png | 256x191 | 214.0 | tg-6285306818012912747 |
| 36 | 🥲 | image/png | 256x191 | 203.8 | tg-6284954381586534901 |
| 37 | 🥰 | image/png | 256x256 | 218.1 | tg-6285322507528441984 |
| 38 | 😫 | image/png | 256x256 | 212.0 | tg-6285316382905077438 |
| 39 | 🥰 | image/png | 256x256 | 222.3 | tg-6284982711190818388 |
| 40 | 🥰 | image/png | 256x244 | 303.6 | tg-6285128108718689981 |
| 41 | 😆 | image/png | 256x256 | 193.6 | tg-6285252843158901915 |
| 42 | 😟 | image/png | 256x256 | 221.7 | tg-6284880993480348029 |
| 43 | 😉 | image/png | 256x256 | 194.7 | tg-6284784691723636608 |
| 44 | 😄 | image/png | 256x256 | 200.7 | tg-6284837086029681444 |
| 45 | 😫 | image/png | 256x256 | 226.7 | tg-6284819545383243249 |
| 46 | 😏 | image/png | 256x256 | 220.2 | tg-6284846861375246428 |
| 47 | ⭐ | image/png | 256x256 | 239.6 | tg-6285202441717682007 |
| 48 | 😃 | image/png | 256x256 | 234.3 | tg-6282914108912177326 |
| 49 | 🔥 | image/png | 256x256 | 325.9 | tg-6284962778247598622 |
| 50 | 🔥 | image/png | 256x256 | 328.2 | tg-6285025214187180756 |
| 51 | 🔥 | image/png | 256x256 | 321.6 | tg-6285296875163619097 |
| 52 | 👍 | image/png | 256x256 | 270.4 | tg-6136553249940967654 |
| 53 | 👍 | image/png | 256x256 | 356.8 | tg-6134281478529355869 |
| 54 | 🥲 | image/png | 256x256 | 315.0 | tg-6172621049557949225 |
| 55 | 🙂 | image/png | 256x256 | 269.3 | tg-6174935061972915303 |
| 56 | 👓 | image/png | 256x256 | 265.7 | tg-6091658334753004777 |
| 57 | 👓 | image/png | 256x256 | 257.2 | tg-6093527577534669467 |
| 58 | 👄 | image/png | 256x256 | 360.2 | tg-6091256557742333111 |
| 59 | 👂 | image/png | 256x256 | 342.4 | tg-6091291389927104528 |
| 60 | 👂 | image/png | 256x256 | 297.6 | tg-6091456544304536561 |
| 61 | 📖 | image/png | 256x256 | 265.4 | tg-6093602876901301737 |
| 62 | 👄 | image/png | 256x256 | 226.2 | tg-6093565283052560758 |
| 63 | 👂 | image/png | 256x256 | 232.8 | tg-6093500957327367353 |
| 64 | 🤒 | image/png | 256x256 | 286.9 | tg-6093725223339696141 |
| 65 | 🤒 | image/png | 256x256 | 273.0 | tg-6091347688358420399 |
| 66 | 🥰 | image/png | 256x256 | 234.4 | tg-6093757813551540265 |
| 67 | ☺️ | image/png | 256x256 | 237.4 | tg-6093733242043638301 |
| 68 | ☹️ | image/png | 256x256 | 277.7 | tg-6091241203234250765 |
| 69 | 🤬 | image/png | 256x256 | 299.3 | tg-6093445955976176719 |


## 48. `AliceInCradle@Sakuraba_O` — `aic02.json`

- 標題:`AliceInCradle@Sakuraba_O`;包 ID:`tg-2814589032237891582`
- 張數:52;mimetype 分佈:image/png ×52
- 大小統計:合計 13,870,245 B(13.23 MB);平均 260.5 KB;最小 30.1 KB;最大 434.5 KB
- 來源 ID:tg- ×52

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 😟 | image/png | 256x256 | 242.5 | tg-5888596313972413590 |
| 2 | ❤️ | image/png | 256x256 | 276.8 | tg-5886206143197352551 |
| 3 | 😉 | image/png | 256x256 | 248.1 | tg-5888932219069665769 |
| 4 | 😓 | image/png | 256x256 | 227.6 | tg-5889008141206558260 |
| 5 | 🥵 | image/png | 256x256 | 287.5 | tg-5888927975641978488 |
| 6 | 🥬 | image/png | 256x256 | 328.0 | tg-5888960857911596512 |
| 7 | 🫕 | image/png | 256x256 | 289.7 | tg-5886279118986679740 |
| 8 | 😱 | image/png | 256x256 | 392.4 | tg-5888969507975729721 |
| 9 | 😇 | image/png | 256x256 | 355.6 | tg-5888510156928455226 |
| 10 | 😎 | image/png | 256x256 | 425.4 | tg-5888519021740955124 |
| 11 | 🥵 | image/png | 256x256 | 196.2 | tg-5888523157794460597 |
| 12 | 🤯 | image/png | 256x256 | 193.1 | tg-5888887031718746172 |
| 13 | ☺ | image/png | 256x256 | 326.7 | tg-5888591241616037393 |
| 14 | 🤔 | image/png | 256x256 | 323.1 | tg-5888853415009719649 |
| 15 | 😡 | image/png | 256x256 | 269.6 | tg-5888990265552672408 |
| 16 | 👍 | image/png | 256x256 | 305.8 | tg-5888580001686623662 |
| 17 | 🥘 | image/png | 256x256 | 306.1 | tg-5888938154714469249 |
| 18 | 😭 | image/png | 256x256 | 332.4 | tg-5888797481650623319 |
| 19 | 😏 | image/png | 256x256 | 292.9 | tg-5891086548895537155 |
| 20 | 😰 | image/png | 256x256 | 333.2 | tg-5888622624942068865 |
| 21 | 🥰 | image/png | 256x256 | 360.7 | tg-5888807196866647223 |
| 22 | 👍 | image/png | 256x256 | 322.2 | tg-5888625184742578209 |
| 23 | 😴 | image/png | 256x256 | 267.1 | tg-5888911908169324543 |
| 24 | 🤑 | image/png | 256x256 | 417.9 | tg-5890727648543380606 |
| 25 | 😰 | image/png | 256x256 | 325.2 | tg-5891033274121196408 |
| 26 | 🤔 | image/png | 256x256 | 326.2 | tg-5890751142014489682 |
| 27 | 👍 | image/png | 256x256 | 310.5 | tg-5890966663473404113 |
| 28 | 🖼 | image/png | 256x256 | 378.6 | tg-5893503992712926370 |
| 29 | 🙂 | image/png | 256x256 | 306.5 | tg-5890813298781196739 |
| 30 | 😨 | image/png | 256x256 | 308.7 | tg-5890999404009100994 |
| 31 | 👩‍🦽 | image/png | 256x256 | 434.5 | tg-5895422850956793800 |
| 32 | 🥵 | image/png | 256x256 | 196.8 | tg-5897683644431998036 |
| 33 | 🥵 | image/png | 256x256 | 202.7 | tg-5897793617069610197 |
| 34 | 🥵 | image/png | 256x256 | 191.7 | tg-5897926812595392920 |
| 35 | 🥺 | image/png | 256x256 | 287.8 | tg-5897952290341393434 |
| 36 | 😡 | image/png | 256x256 | 192.5 | tg-5900132316956595291 |
| 37 | 😡 | image/png | 256x256 | 183.4 | tg-5897722711454520497 |
| 38 | 😡 | image/png | 256x256 | 190.1 | tg-5897610625692996637 |
| 39 | 🫨 | image/png | 256x256 | 160.7 | tg-6030630122241923109 |
| 40 | 🤨 | image/png | 256x256 | 30.1 | tg-6030607401864927253 |
| 41 | 😡 | image/png | 256x256 | 168.8 | tg-6028519519478092990 |
| 42 | 🫨 | image/png | 256x256 | 196.2 | tg-6028125670977049509 |
| 43 | 😣 | image/png | 256x256 | 183.2 | tg-6028127912949976661 |
| 44 | 😣 | image/png | 256x256 | 181.8 | tg-6030772947084383334 |
| 45 | 😓 | image/png | 256x256 | 190.1 | tg-6028168036534457793 |
| 46 | 🤗 | image/png | 256x256 | 141.2 | tg-6030383865997041141 |
| 47 | 😡 | image/png | 256x256 | 177.7 | tg-6028079663287375778 |
| 48 | ☺ | image/png | 256x256 | 187.7 | tg-6028073134937084350 |
| 49 | 🤨 | image/png | 256x256 | 185.8 | tg-6030554938839406116 |
| 50 | 😓 | image/png | 256x256 | 206.5 | tg-6030824748684940856 |
| 51 | 🥪 | image/png | 189x256 | 160.3 | tg-6030528954287264998 |
| 52 | 🫣 | image/png | 256x256 | 219.2 | tg-6030857154213189118 |


## 49. `琪露诺` — `qi2_lu4_nuo4_by_fStikBot.json`

- 標題:`琪露诺`;包 ID:`tg-4268808458368712703`
- 張數:120;mimetype 分佈:image/png ×99;video/webm ×21
- 大小統計:合計 25,723,985 B(24.53 MB);平均 209.3 KB;最小 8.0 KB;最大 513.5 KB
- 來源 ID:tg- ×120

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🌟 | image/png | 205x256 | 217.4 | tg-6289734628647376615 |
| 2 | 🥳 | video/webm | 512x291 | 183.4 | tg-6289356315043043959 |
| 3 | 👍 | image/png | 256x256 | 212.1 | tg-6291750295454095867 |
| 4 | ❤️ | image/png | 256x256 | 168.5 | tg-6292017274916181151 |
| 5 | 🛏 | image/png | 256x256 | 169.3 | tg-6289391752818201698 |
| 6 | 😀 | image/png | 256x228 | 186.0 | tg-6291831457451087712 |
| 7 | 😸 | image/png | 256x256 | 297.3 | tg-6289754716209420049 |
| 8 | 🌟 | video/webm | 512x381 | 8.0 | tg-6291554333276248075 |
| 9 | 👍 | image/png | 256x256 | 226.9 | tg-6291555544457025360 |
| 10 | 😭 | image/png | 256x256 | 213.3 | tg-6289791897741301698 |
| 11 | ❤️ | image/png | 256x256 | 178.7 | tg-6289431829158041634 |
| 12 | ❤️ | image/png | 256x256 | 155.3 | tg-6289542020838989514 |
| 13 | 🔓 | image/png | 256x256 | 225.8 | tg-6289728289275647289 |
| 14 | 👶 | image/png | 256x256 | 178.8 | tg-6289459226754422645 |
| 15 | 👶 | image/png | 256x256 | 145.3 | tg-6291897780336073930 |
| 16 | 📌 | image/png | 256x256 | 203.8 | tg-6289479348676205475 |
| 17 | 🤔 | image/png | 256x256 | 223.8 | tg-6289722005738494502 |
| 18 | 👀 | image/png | 256x256 | 82.4 | tg-6291914062557091632 |
| 19 | ❤️ | image/png | 256x256 | 204.3 | tg-6289824981874382323 |
| 20 | ⬆️ | image/png | 256x256 | 162.5 | tg-6292002951200249208 |
| 21 | ⬇️ | image/png | 256x256 | 117.0 | tg-6289655931961612562 |
| 22 | 😆 | video/webm | 476x512 | 119.8 | tg-6289313352485181780 |
| 23 | 👊 | video/webm | 512x512 | 113.4 | tg-6289603408806549811 |
| 24 | 😆 | video/webm | 512x288 | 196.2 | tg-6289335411437213871 |
| 25 | 😞 | image/png | 256x203 | 178.6 | tg-6289545061675833883 |
| 26 | ❓ | image/png | 256x239 | 258.7 | tg-6291615755603548025 |
| 27 | 🌟 | image/png | 256x256 | 334.2 | tg-6291641396558304493 |
| 28 | 😆 | image/png | 256x170 | 100.9 | tg-6292006666346959947 |
| 29 | 😆 | image/png | 240x256 | 212.0 | tg-6289319859360635201 |
| 30 | 🌟 | image/png | 238x256 | 199.3 | tg-6291587048042140937 |
| 31 | 🤪 | image/png | 256x256 | 127.2 | tg-6291607749784507344 |
| 32 | 😃 | image/png | 256x256 | 224.7 | tg-6289309688878078564 |
| 33 | 👻 | image/png | 256x210 | 323.2 | tg-6292065524578784628 |
| 34 | 😫 | image/png | 256x256 | 190.7 | tg-6291701758028682992 |
| 35 | 😖 | image/png | 256x256 | 168.6 | tg-6291868428529571551 |
| 36 | 😢 | image/png | 256x256 | 164.3 | tg-6291925594544281630 |
| 37 | 😝 | image/png | 256x256 | 174.2 | tg-6292022824013929279 |
| 38 | 😁 | image/png | 256x256 | 339.0 | tg-6289294484693850317 |
| 39 | 😢 | image/png | 256x256 | 335.3 | tg-6292078860452239713 |
| 40 | 😴 | image/png | 256x256 | 317.1 | tg-6289435320966453058 |
| 41 | ☺️ | image/png | 256x256 | 353.0 | tg-6289312819909236124 |
| 42 | 😠 | image/png | 256x256 | 264.4 | tg-6289477441710725787 |
| 43 | 😭 | image/png | 256x256 | 384.4 | tg-6289587972694087290 |
| 44 | 👋 | video/webm | 474x512 | 41.2 | tg-6289383313207465939 |
| 45 | 🤯 | video/webm | 512x494 | 227.1 | tg-6289393299006430119 |
| 46 | 🙂 | video/webm | 512x512 | 187.9 | tg-6289424373094816457 |
| 47 | 🙂 | video/webm | 512x286 | 165.5 | tg-6289578738514401394 |
| 48 | 🎂 | image/png | 256x256 | 255.7 | tg-6291674222993347562 |
| 49 | 🤙 | image/png | 256x256 | 335.8 | tg-6289736574267561841 |
| 50 | 👍 | video/webm | 512x438 | 157.0 | tg-6291986059093874545 |
| 51 | 👍 | video/webm | 512x493 | 101.1 | tg-6291948237611865987 |
| 52 | 🌚 | image/png | 204x256 | 101.4 | tg-6291615631049496401 |
| 53 | 😕 | image/png | 256x218 | 164.0 | tg-6291767582697461990 |
| 54 | 🙂 | image/png | 256x145 | 238.2 | tg-6289358200533686701 |
| 55 | 🤪 | image/png | 256x246 | 230.1 | tg-6291719616502700579 |
| 56 | 🧊 | video/webm | 322x512 | 137.2 | tg-6329856654053480824 |
| 57 | 🧊 | video/webm | 512x512 | 152.7 | tg-6332594639870106369 |
| 58 | 🧊 | video/webm | 512x512 | 157.7 | tg-6330160789277645184 |
| 59 | 🧊 | video/webm | 512x288 | 177.4 | tg-6332135632420214382 |
| 60 | 🧊 | video/webm | 512x390 | 152.9 | tg-6332276683441182252 |
| 61 | 🧊 | video/webm | 512x288 | 137.2 | tg-6332466834528277908 |
| 62 | 🧊 | video/webm | 512x363 | 141.0 | tg-6332339295474424599 |
| 63 | 🧊 | video/webm | 512x276 | 86.5 | tg-6332348710042736613 |
| 64 | 🧊 | video/webm | 512x512 | 71.0 | tg-6332474123087785559 |
| 65 | 🍵 | image/png | 256x256 | 247.7 | tg-6091274506410662132 |
| 66 | 👍 | image/png | 256x256 | 181.9 | tg-6088950950578362320 |
| 67 | 👍 | image/png | 256x256 | 183.7 | tg-6091341572324989170 |
| 68 | 👍 | image/png | 256x256 | 174.9 | tg-6091119144558664758 |
| 69 | 👍 | image/png | 256x256 | 163.9 | tg-6089123260371310459 |
| 70 | 👍 | image/png | 256x256 | 141.1 | tg-6091626667959131063 |
| 71 | 👍 | image/png | 256x256 | 172.4 | tg-6091220784959725544 |
| 72 | 🌟 | video/webm | 512x512 | 84.9 | tg-6089004367086623340 |
| 73 | 👍 | image/png | 256x256 | 237.2 | tg-6091602040616655158 |
| 74 | 🌸 | image/png | 256x256 | 201.4 | tg-6091260354493421893 |
| 75 | 👄 | image/png | 256x256 | 336.3 | tg-6093436232170215742 |
| 76 | 👄 | image/png | 256x256 | 268.8 | tg-6093425013715639520 |
| 77 | 📖 | image/png | 256x256 | 427.7 | tg-6093886971808060984 |
| 78 | 🍲 | image/png | 256x256 | 149.3 | tg-6091354448636942801 |
| 79 | 👄 | image/png | 256x256 | 198.1 | tg-6093652170240956141 |
| 80 | 👄 | image/png | 256x256 | 176.2 | tg-6093454515845994333 |
| 81 | 🧸 | image/png | 256x256 | 297.3 | tg-6091657935321045175 |
| 82 | 👍 | image/png | 256x256 | 256.1 | tg-6093445122752519954 |
| 83 | 👄 | image/png | 256x256 | 193.7 | tg-6093683502027380506 |
| 84 | 👍 | image/png | 256x256 | 311.2 | tg-6100310456176483431 |
| 85 | 👍 | image/png | 256x256 | 190.8 | tg-6098048064973445943 |
| 86 | 👓 | image/png | 256x256 | 177.8 | tg-6097900932278785500 |
| 87 | 🚗 | image/png | 256x256 | 146.5 | tg-6098181445182826691 |
| 88 | 👓 | image/png | 256x256 | 142.1 | tg-6100130686025341113 |
| 89 | 🐱 | image/png | 256x256 | 186.7 | tg-6100380146315827284 |
| 90 | ✋ | image/png | 256x256 | 220.7 | tg-6098348635374753472 |
| 91 | 🧸 | image/png | 256x256 | 132.4 | tg-6100310872788310625 |
| 92 | 👄 | image/png | 256x256 | 296.7 | tg-6100130514226648698 |
| 93 | 🐦 | image/png | 256x256 | 513.5 | tg-6098361945478404865 |
| 94 | 🎢 | image/png | 256x256 | 240.8 | tg-6100492425350879628 |
| 95 | 👄 | image/png | 256x256 | 196.1 | tg-6100129187081754426 |
| 96 | ✋ | image/png | 256x256 | 340.7 | tg-6098241132343335825 |
| 97 | 🧸 | image/png | 256x256 | 184.9 | tg-6098228380585437465 |
| 98 | 🔳 | image/png | 256x256 | 247.9 | tg-6097932749396514798 |
| 99 | 🧸 | image/png | 256x256 | 248.4 | tg-6098060082291940282 |
| 100 | 🧸 | image/png | 256x256 | 166.1 | tg-6100424294284662896 |
| 101 | 🎩 | image/png | 256x256 | 188.6 | tg-6100254308069021486 |
| 102 | 👄 | image/png | 256x256 | 223.4 | tg-6098277888673453825 |
| 103 | 🧸 | image/png | 256x256 | 328.1 | tg-6100600817440528239 |
| 104 | 🧸 | image/png | 256x256 | 223.6 | tg-6097882326480460668 |
| 105 | 📖 | image/png | 256x256 | 262.8 | tg-6100598163150739846 |
| 106 | 💇 | image/png | 256x256 | 231.3 | tg-6100460526628772770 |
| 107 | 💇 | image/png | 256x256 | 228.6 | tg-6100338953284491889 |
| 108 | 📦 | image/png | 256x256 | 73.8 | tg-6100240559878708270 |
| 109 | 🎢 | image/png | 256x256 | 331.1 | tg-6100667410908452938 |
| 110 | 👄 | image/png | 256x256 | 195.7 | tg-6097893407496083223 |
| 111 | 🩳 | image/png | 256x256 | 213.9 | tg-6100597286977410879 |
| 112 | 👄 | image/png | 256x256 | 236.0 | tg-6098417595369659417 |
| 113 | 🧸 | image/png | 256x256 | 328.3 | tg-6100185511282874563 |
| 114 | 🐶 | image/png | 256x256 | 241.1 | tg-6100519891666737443 |
| 115 | 🪑 | image/png | 256x256 | 224.0 | tg-6100441315240056981 |
| 116 | 🍲 | image/png | 256x256 | 241.7 | tg-6100367527701912179 |
| 117 | 👄 | image/png | 256x256 | 247.2 | tg-6100386318183831904 |
| 118 | 👍 | image/png | 256x256 | 250.3 | tg-6100265290300397284 |
| 119 | 👍 | image/png | 256x256 | 158.9 | tg-6100671907739210946 |
| 120 | 👍 | image/png | 256x256 | 398.9 | tg-6107042654204204415 |


## 50. `Sticker Leaking NEW :: @fStikBot` — `Sticker_Leaking_NEWW_by_fStikBot.json`

- 標題:`Sticker Leaking NEW :: @fStikBot`;包 ID:`tg-381568008427929603`
- 張數:65;mimetype 分佈:image/png ×65
- 大小統計:合計 7,977,734 B(7.61 MB);平均 119.9 KB;最小 17.1 KB;最大 467.3 KB
- 來源 ID:tg- ×65

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 🚰 | image/png | 256x54 | 70.9 | tg-6280455961689724656 |
| 2 | 🤖️ | image/png | 256x93 | 42.7 | tg-6282767903930455369 |
| 3 | 🔧 | image/png | 256x256 | 243.5 | tg-6280716838003283834 |
| 4 | 🪟 | image/png | 256x33 | 43.7 | tg-6280314120394774193 |
| 5 | ❓ | image/png | 256x31 | 62.8 | tg-6280566849155372204 |
| 6 | ❗️ | image/png | 256x38 | 67.2 | tg-6280466621798552399 |
| 7 | 👌 | image/png | 254x256 | 279.5 | tg-6280483462365321054 |
| 8 | 🪣 | image/png | 256x50 | 64.8 | tg-6280690741781992769 |
| 9 | 🔋 | image/png | 256x28 | 58.6 | tg-6280557473241765891 |
| 10 | 🔥 | image/png | 256x144 | 216.4 | tg-6280635310934070842 |
| 11 | 🔥 | image/png | 256x144 | 208.2 | tg-6280392211490149811 |
| 12 | 🈲️ | image/png | 256x87 | 40.9 | tg-6280582684699792872 |
| 13 | 🔚 | image/png | 243x256 | 17.1 | tg-6280558379479865230 |
| 14 | 👍 | image/png | 256x127 | 227.5 | tg-6280536586815805013 |
| 15 | 👍 | image/png | 256x129 | 207.1 | tg-6280577380415181592 |
| 16 | 🈲️ | image/png | 256x147 | 80.0 | tg-6282683314549560109 |
| 17 | 🌟 | image/png | 256x147 | 55.7 | tg-6064431360242620890 |
| 18 | 🪣 | image/png | 256x57 | 97.1 | tg-6280674592704961117 |
| 19 | 🚰 | image/png | 256x33 | 62.4 | tg-6282538690115801665 |
| 20 | 🚰 | image/png | 256x39 | 76.9 | tg-6282580797975172969 |
| 21 | 🌐 | image/png | 256x29 | 56.6 | tg-6280448501331533707 |
| 22 | 🕶 | image/png | 256x44 | 84.5 | tg-6280694663087134287 |
| 23 | 🙋‍♀ | image/png | 256x77 | 103.9 | tg-6282932650285995240 |
| 24 | 🔎 | image/png | 256x39 | 65.1 | tg-6280413351319180721 |
| 25 | 🌟 | image/png | 256x144 | 256.0 | tg-6280385485571364046 |
| 26 | 🌟 | image/png | 256x55 | 75.2 | tg-6280423002110694553 |
| 27 | 🌟 | image/png | 256x79 | 40.0 | tg-6280806959302055862 |
| 28 | 🌟 | image/png | 256x79 | 36.8 | tg-6280615794602677720 |
| 29 | 🌟 | image/png | 256x79 | 29.0 | tg-6280583560873121294 |
| 30 | 🌟 | image/png | 256x79 | 37.9 | tg-6282758377692993278 |
| 31 | 🌟 | image/png | 256x144 | 160.9 | tg-6282569270282949760 |
| 32 | 🌟 | image/png | 256x191 | 312.8 | tg-6280448600115778905 |
| 33 | 😅 | image/png | 256x105 | 66.8 | tg-6280716077794071922 |
| 34 | 🌟 | image/png | 256x36 | 63.1 | tg-6280710322537895857 |
| 35 | 🌟 | image/png | 256x45 | 82.3 | tg-6280562133281281667 |
| 36 | 🌟 | image/png | 256x79 | 30.5 | tg-6280773299643356737 |
| 37 | 🌟 | image/png | 256x101 | 36.3 | tg-6280443905716524725 |
| 38 | 🌟 | image/png | 256x111 | 67.9 | tg-6282820186567349604 |
| 39 | 🌟 | image/png | 256x115 | 83.5 | tg-6280389690344348746 |
| 40 | 🌟 | image/png | 256x119 | 84.9 | tg-6280637746180528595 |
| 41 | 🌟 | image/png | 256x34 | 68.0 | tg-6280273468529318015 |
| 42 | 🌟 | image/png | 256x36 | 62.6 | tg-6282539020828284580 |
| 43 | 🌟 | image/png | 256x229 | 342.8 | tg-6283058939504367031 |
| 44 | 🌟 | image/png | 256x229 | 315.5 | tg-6282926319504202044 |
| 45 | 🌟 | image/png | 256x144 | 216.1 | tg-6280309494714996863 |
| 46 | 🌟 | image/png | 256x59 | 93.7 | tg-6287391702512571043 |
| 47 | 🌟 | image/png | 256x144 | 217.9 | tg-6291954701537646037 |
| 48 | 🌟 | image/png | 256x191 | 102.2 | tg-6055591608877847626 |
| 49 | 🌟 | image/png | 256x129 | 60.2 | tg-6055369666442829645 |
| 50 | 🌟 | image/png | 256x105 | 130.0 | tg-6190257473765512826 |
| 51 | 🌟 | image/png | 256x44 | 68.1 | tg-6192934629960324766 |
| 52 | 🌟 | image/png | 256x93 | 104.5 | tg-6192556887586642057 |
| 53 | 🌟 | image/png | 256x41 | 77.2 | tg-6190588276441617721 |
| 54 | 🌟 | image/png | 256x174 | 188.3 | tg-6195022812994868574 |
| 55 | 🚰 | image/png | 256x256 | 467.3 | tg-6271593580142269699 |
| 56 | 🌟 | image/png | 256x143 | 40.3 | tg-6201723073645778618 |
| 57 | 🌟 | image/png | 256x144 | 242.6 | tg-6242078062372985785 |
| 58 | 🌟 | image/png | 221x256 | 238.1 | tg-6069089299519773726 |
| 59 | 🌟 | image/png | 256x144 | 160.7 | tg-6093759432754208726 |
| 60 | 🌟 | image/png | 256x168 | 157.9 | tg-6106917279813867532 |
| 61 | 🌟 | image/png | 256x49 | 86.2 | tg-6109576573239695432 |
| 62 | 🌟 | image/png | 256x27 | 58.7 | tg-6111945350782654943 |
| 63 | 💦 | image/png | 256x256 | 75.9 | tg-6122786320684161607 |
| 64 | 🌟 | image/png | 256x60 | 132.1 | tg-6163261014444875276 |
| 65 | 🌟 | image/png | 256x43 | 86.7 | tg-6183719236460878944 |


## 51. `USA best::@aerodynamic39` — `USABest.json`

- 標題:`USA best::@aerodynamic39`;包 ID:`tg-7113950934484385788`
- 張數:0(**空包** — JSON 內 `stickers` 陣列為空,無逐張列表可列)
- mimetype 分佈:無(空包)
- 大小統計:無(空包)


## 52. `@sticker_freehk 超かぐや姫！ Pack1` — `Cosmic_Princess_Kaguya_Pack1.json`

- 標題:`@sticker_freehk 超かぐや姫！ Pack1`;包 ID:`tg-4784764838154862777`
- 張數:1;mimetype 分佈:video/webm ×1
- 大小統計:合計 32,255 B(0.03 MB);平均 31.5 KB;最小 31.5 KB;最大 31.5 KB
- 來源 ID:tg- ×1

逐張列表:

| # | body(名稱/表情) | mimetype | 尺寸(WxH) | 大小(KB) | 來源 ID |
|---:|---|---|---|---:|---|
| 1 | 😓 | video/webm | 512x512 | 31.5 | tg-6325706435745292095 |


## 53. `kipfel | by @xy_Stickers` — `kawaiikipfel_by_moe_sticker_bot.json`

- 標題:`kipfel | by @xy_Stickers`;包 ID:`tg-5487586882676064264`
- 張數:0(**空包** — JSON 內 `stickers` 陣列為空,無逐張列表可列)
- mimetype 分佈:無(空包)
- 大小統計:無(空包)


## 54. `Mygo Sticker Twi:Asahi_rise` — `MygoStickerByAsahiRise.json`

- 標題:`Mygo Sticker Twi:Asahi_rise`;包 ID:`tg-5031608235132452904`
- 張數:0(**空包** — JSON 內 `stickers` 陣列為空,無逐張列表可列)
- mimetype 分佈:無(空包)
- 大小統計:無(空包)

---

## 五、編纂後記

- 逐張列表總列數:3,149(與全庫總張數一致)
- 包章節數:54(含 3 個空包章節:USABest、kawaiikipfel_by_moe_sticker_bot、MygoStickerByAsahiRise)
- 來源 ID 分佈:tg- ×2,321;sha256(外) ×828
- 異常張(零尺寸或 <500 B):0 張
- 畸形貼圖 `tg-692497273854099475`(256x0)確認不在 stneng.json 亦不在全庫任何位置
- 本目錄所有數字均由 54 個 JSON 原始資料即時計算產生,非人工抄錄。
