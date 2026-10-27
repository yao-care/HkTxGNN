---
layout: default
title: Tetracaine
parent: 僅模型預測 (L5)
nav_order: 867
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Tetracaine：預測新適應症為慢性萎縮性肢端皮膚炎 (Acrodermatitis chronica atrophicans)（證據等級 L5）。原適應症：皮膚炎 (dermatitis)"
monitor_inn: "TETRACAINE"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "bronchitis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid"]
---

# Tetracaine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Tetracaine：從皮膚炎到慢性萎縮性肢端皮膚炎
{: .text-alpha }

## 一句話總結

Tetracaine 是一種酯類局部麻醉藥，在知識圖譜中的原適應症為皮膚炎 (dermatitis)。
TxGNN 模型預測它可能對**慢性萎縮性肢端皮膚炎 (Acrodermatitis chronica atrophicans)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個預測，僅屬模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 皮膚炎 (dermatitis)（來自知識圖譜；香港許可證未載明核准適應症文字） |
| 預測新適應症 | 慢性萎縮性肢端皮膚炎 (Acrodermatitis chronica atrophicans) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般而言，Tetracaine 是局部麻醉藥，作用在於阻斷鈉離子通道，能提供局部止痛，但這項資訊並非來自本報告所整理的資料，僅作背景參考。

慢性萎縮性肢端皮膚炎是萊姆病（伯氏疏螺旋體感染）的晚期皮膚表現，標準治療為全身性抗生素。Tetracaine 沒有抗菌活性，預期無法改變疾病本身。

因此，這個高分預測較可能反映知識圖譜中與原適應症（皮膚炎）的相近關係，而非有生物學依據。目前未建立任何機轉連結。

排名第 2 至第 5 的預測（新生兒皮肌炎、支氣管炎、兒童結締組織病相關次發性間質性肺病、瘢痕疙瘩性痤瘡）同樣缺乏機轉支持。其中僅「瘢痕疙瘩性痤瘡」有間接資料，內容為雷射治療時的麻醉止痛，並非疾病治療。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

（補充：排名第 5 的「瘢痕疙瘩性痤瘡」有 1 項間接相關試驗 [NCT02372786](https://clinicaltrials.gov/study/NCT02372786)，為 Phase 4、已完成、30 人的雙盲隨機試驗，比較 7% 利多卡因/7% 丁卡因乳膏與 2.5% 利多卡因/2.5% 丙胺卡因乳膏於雷射治療時的止痛效果。它評估的是程序性麻醉，並非疾病治療。）

---

## 文獻證據

目前無相關文獻。

（補充：排名第 5 的預測有 1 篇間接相關文獻 [27377616](https://pubmed.ncbi.nlm.nih.gov/27377616/)，為 2017 年發表於 The British Journal of Dermatology 的 RCT，比較利多卡因/丁卡因乳膏與利多卡因/丙胺卡因乳膏，用於瘢痕疙瘩性痤瘡及刺青去除雷射治療時的局部麻醉，結論僅涉及止痛。）

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-54171 | MINIMS TETRACAINE HYDROCHLORIDE EYE DROPS 1% (LAB CHAUVIN) | 未提供 | 未提供 |
| HK-63840 | PLIAGLIS CREAM | 未提供 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的相關疾病（非仿單文字）**：癲癇、腎臟疾病、肝臟疾病、膽囊疾病、心臟疾病（含心血管疾病、心臟猝停、心臟傳導疾病）、呼吸衰竭、重症肌無力與神經肌肉接合部疾病、丁醯膽鹼酯酶缺乏症、甲狀腺機能亢進（含葛瑞夫茲氏病、甲狀腺毒症）、葡萄膜炎及虹膜、睫狀體相關疾病、眼部感染性疾病、結膜炎。這些來自圖譜的禁忌關聯，需對照正式仿單確認。
- **藥物交互作用**：共 32 筆紀錄（以下為已提供的清單）：
  - **嚴重 (Major)**：亞硝酸 (Nitrous acid)、Bupivacaine (liposome)
  - **中度 (Moderate)**：Sulfasalazine、Sulfamethoxazole、Lidocaine（外用/眼用）、Benzocaine、Cocaine（外用/鼻用）、Proparacaine、Oxybuprocaine、Cinchocaine，以及苯二氮平類（Alprazolam、Chlordiazepoxide、Clobazam、Clonazepam、Clorazepic acid、Diazepam、Estazolam）
  - **輕微 (Minor)**：Hyaluronidase
- **其他考量**：若用於新生兒或兒童，需注意全身吸收與高鐵血紅素血症風險。若用於呼吸道，需注意吸入性風險、保護性反射喪失與全身毒性。

仿單的主要警語與禁忌症資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症僅有模型分數，沒有直接的臨床或機轉證據，證據等級為 L5。對慢性萎縮性肢端皮膚炎，標準治療是抗生素，Tetracaine 沒有抗菌作用。
- 唯一有間接資料的是「瘢痕疙瘩性痤瘡」（L4，列為研究問題），但證據僅關於程序性止痛，並非治療疾病。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症（目前為阻擋性資料缺口）
- 補充 DrugBank 作用機轉資料
- 若欲探索，可將「雷射或侵入性處置時的輔助麻醉」重新定義為研究問題，而非疾病治療適應症
- 確認許可證的核准適應症與劑型（目前皆為空白），並評估給藥途徑是否與預測適應症相容
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

