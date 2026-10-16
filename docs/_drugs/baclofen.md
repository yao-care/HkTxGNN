---
layout: default
title: Baclofen
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Baclofen：預測新適應症為注意力不足過動症 (Attention Deficit-Hyperactivity Disorder)（證據等級 L5）。原適應症：本次彙整資料中未載明"
---

# Baclofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Baclofen：從痙攣（原適應症資料缺漏）到注意力不足過動症／尼古丁依賴

注意：本報告依資料以 predicted_indications[0]（注意力不足過動症）為主要預測。另一個排名第 2 的預測（尼古丁依賴）證據明顯較多，我也一併列出供參考。

## 一句話總結

Baclofen 是 GABA-B 受體促效劑，在香港有 12 張有效許可證，但本次彙整的資料中未載明核准適應症文字。
TxGNN 模型預測它可能對**注意力不足過動症 (ADHD)** 有效（分數 99.3%），但目前**沒有臨床試驗**，且 9 篇文獻中沒有任何一篇直接研究 baclofen 用於 ADHD。
另一個預測**尼古丁依賴 (Nicotine Dependence)** 有 **3 個 Phase 2 臨床試驗**和多篇文獻，證據相對較多。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次彙整資料中未載明 |
| 預測新適應症 | 注意力不足過動症 (Attention Deficit-Hyperactivity Disorder) |
| TxGNN 預測分數 | 99.32% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 12 張 |
| 建議決策 | Hold |

**對照：尼古丁依賴**（TxGNN 分數 99.19%，證據等級 L2，建議為「研究問題」，需審慎看待，因試驗規模小且多數提前終止）。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 baclofen 是 GABA-B 受體促效劑，可能調節皮質與紋狀體的興奮／抑制平衡以及多巴胺訊號，而這些與衝動性和注意力有關。但這是依機轉所做的推論，並未被現有證據證實。

檢索到的文獻主要涉及成人 ADHD 的 methylphenidate 處方、妥瑞氏症與抽動症治療，以及齧齒類動物的衝動決策神經迴路研究。這些與 baclofen 治療 ADHD 並無直接關聯。模型的高分可能來自與妥瑞氏症等神經精神疾病在知識圖譜上的相近性。

至於尼古丁依賴，GABA-B 活化可抑制中腦邊緣多巴胺釋放與獎賞訊號，機轉上能合理解釋對尼古丁獎賞、渴求與戒斷的影響。大鼠實驗也顯示 baclofen 可減弱尼古丁的獎賞效應與戒斷表現。

## 臨床試驗證據

**注意力不足過動症：** 目前無相關臨床試驗登記。

**尼古丁依賴（對照）：**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01228994](https://clinicaltrials.gov/study/NCT01228994) | Phase 2 | 提前終止 | 6 | 檢驗 baclofen 對吸菸者戒菸的效果是否優於安慰劑；僅 6 人，無法評估療效 |
| [NCT00257894](https://clinicaltrials.gov/study/NCT00257894) | Phase 2 | 提前終止 | 41 | 評估 baclofen 對中重度吸菸者吸菸衝動、戒斷與強化效果的影響；提前終止，解讀受限 |
| [NCT01821560](https://clinicaltrials.gov/study/NCT01821560) | Phase 2 | 完成 | 44 | 以 fMRI 探討 baclofen 對吸菸者腦部與行為反應的影響；規模小，終點非明確戒菸結果 |

所提供的紀錄中沒有療效結果，故臨床效益無法確認。

## 文獻證據

**注意力不足過動症（皆非直接研究 baclofen 於 ADHD）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Review | L'Encephale | 成人 ADHD 的 methylphenidate 超適應症處方管理 |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | Int Rev Neurobiol | 妥瑞氏症新興治療策略 |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatr Drugs | 妥瑞氏症臨床特徵與處置策略 |
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Review | Cureus | 行為介入、抗精神病藥與 α 促效劑治療妥瑞氏症抽動 |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Review | J Child Neurol | 450 名抽動症／妥瑞氏症患者使用 baclofen／肉毒桿菌毒素治療的報告 |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | 動物實驗 | Psychopharmacology | α2A 腎上腺素受體刺激可降低衝動決策 |

**尼古丁依賴（對照，節選）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29250815](https://pubmed.ncbi.nlm.nih.gov/29250815/) | 2018 | Review | Pharmacotherapy | 現有與新興戒菸藥物治療 |
| [24654737](https://pubmed.ncbi.nlm.nih.gov/24654737/) | 2014 | Review | Expert Opin Emerg Drugs | 菸害依賴新興藥物 |
| [11841892](https://pubmed.ncbi.nlm.nih.gov/11841892/) | 2002 | Review | Drug Alcohol Depend | GABA-B 促效劑可能降低多種成癮藥物的使用 |
| [24553576](https://pubmed.ncbi.nlm.nih.gov/24553576/) | 2014 | 動物實驗 | Psychopharmacology | Baclofen 減弱尼古丁獎賞與戒斷表現 |
| [18682277](https://pubmed.ncbi.nlm.nih.gov/18682277/) | 2008 | 動物實驗 | Neurosci Lett | 不同劑量 baclofen 對大鼠尼古丁條件性位置偏好的影響 |
| [19250803](https://pubmed.ncbi.nlm.nih.gov/19250803/) | 2009 | 動物實驗 | Eur Neuropsychopharmacol | Baclofen 預防尼古丁尋求行為復發 |
| [25868070](https://pubmed.ncbi.nlm.nih.gov/25868070/) | 2015 | RCT（摘要） | Neuropsychopharmacology | Baclofen 用於酒精與尼古丁共病依賴的雙盲安慰劑對照試驗 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66213 | BACLOFEN INTRATHECAL SINTETICA 輸注液 40MG/20ML | 未載明 | 未載明 |
| HK-66245 | BACLOFEN INTRATHECAL SINTETICA 輸注液 10MG/5ML | 未載明 | 未載明 |
| HK-56406 | APT-BACLOFEN TAB 10MG | 錠劑 | 未載明 |
| HK-51460 | LIORESAL INTRATHECAL INJ 10MG/5ML | 注射劑 | 未載明 |
| HK-00226 | LIORESAL 10 TAB 10 MG | 錠劑 | 未載明 |

香港共有 12 張有效單一成分許可證，上表僅列出其中 5 張。

## 安全性考量

- **知識圖譜標示的禁忌疾病（非仿單內容）：** 癲癇、腎臟疾病、精神疾患（含思覺失調症、思覺失調情感性疾患）、腦血管疾患與腦中風、自律神經疾患（含自律神經反射異常）、膀胱頸部疾病等。
- **藥物交互作用：** 共查得 100 筆。主要為嚴重等級的 Morphine（含脂質體嗎啡）；中度等級包括 Dronabinol、Metoclopramide、Nabilone、Opium、Sibutramine、Difenoxin、Diphenoxylate。多為中樞神經抑制相關，合併使用需特別留意。

其他警語與仿單禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold（注意力不足過動症）**

**理由：**
- ADHD 的預測僅有模型分數，沒有臨床試驗，文獻亦無直接證據，證據等級為 L5。
- 此外，知識圖譜標示 baclofen 與精神疾患相關的禁忌，需格外審慎。

**若要推進需要：**
- 取得 baclofen 的詳細作用機轉資料與香港仿單警語、禁忌。
- 針對 ADHD 進行系統性文獻回顧，並先以臨床前或小型探索性研究驗證。
- 評估神經精神安全性（含兒童族群）。
- 若轉向尼古丁依賴：該預測為 L2，但三個 Phase 2 試驗兩個提前終止、樣本小且無療效結果，需設計足夠樣本的 Phase 2b/3 隨機對照試驗，並以戒菸率為主要終點。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

