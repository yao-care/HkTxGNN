---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 779
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Risperidone：預測新適應症為家族性水平凝視麻痺合併進行性脊柱側彎 (gaze palsy, familial horizontal…（證據等級 L5）。原適應症：躁期雙相情感障礙、雙相情感障礙、思覺失調症、自閉症譜系障礙"
monitor_inn: "RISPERIDONE"
predicted_indications: ["gaze palsy, familial horizontal, with progressive scoliosis", "asperger syndrome, susceptibility to", "amelocerebrohypohidrotic syndrome", "Phelan-McDermid syndrome", "trichotillomania"]
---

# Risperidone
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

## Risperidone：從雙相情感障礙與思覺失調症到毛髮拔除症（Trichotillomania）
{: .text-alpha }

## 一句話總結

Risperidone 是一種非典型抗精神病藥，原本用於雙相情感障礙、思覺失調症與自閉症譜系相關症狀。
TxGNN 模型的預測排名第一為罕見的家族性水平凝視麻痺合併進行性脊柱側彎，但該項目完全沒有證據支持。
本報告因此同時說明排名第一的預測，以及證據最完整的**毛髮拔除症 (Trichotillomania)**：目前有 **0 個臨床試驗**，但有 **9 篇文獻**（以個案報告和小型病例系列為主）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 躁期雙相情感障礙、雙相情感障礙、思覺失調症、自閉症譜系障礙（來自知識圖譜；香港許可證未填寫核准適應症文字） |
| 預測新適應症 | 家族性水平凝視麻痺合併進行性脊柱側彎 (gaze palsy, familial horizontal, with progressive scoliosis)，TxGNN 排名第 1 |
| TxGNN 預測分數 | 99.76%（排名第 1 項） |
| 證據等級 | L5（排名第 1 項）；毛髮拔除症為 L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（排名第 1 項）；毛髮拔除症為 Research Question（研究性問題，不建議直接推進臨床使用） |

**本次預測的前五名：**

| 排名 | 預測疾病 | TxGNN 分數 | 證據等級 | 建議 |
|------|---------|-----------|---------|------|
| 1 | 家族性水平凝視麻痺合併進行性脊柱側彎 | 99.76% | L5 | Hold |
| 2 | 亞斯伯格症候群易感性 (Asperger syndrome) | 99.74% | L4 | Hold |
| 3 | 釉質-腦-少汗症候群 (Amelocerebrohypohidrotic syndrome) | 99.69% | L5 | Hold |
| 4 | Phelan-McDermid 症候群 | 99.59% | L4 | Research Question |
| 5 | 毛髮拔除症 (Trichotillomania) | 99.51% | L4 | Research Question |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知的藥理分類，risperidone 主要透過阻斷多巴胺 D2 與血清素 5-HT2A 受體發揮作用，這是通用的藥理知識，並非來自本次彙整資料。

**排名第 1 的預測（家族性水平凝視麻痺合併進行性脊柱側彎）：** 此病為 ROBO3 相關的腦幹軸突導向罕見遺傳疾病。Risperidone 的 D2/5-HT2A 拮抗作用與其病理沒有合理關聯，也沒有任何試驗或文獻。高分僅屬模型的計算結果，不建議視為有效訊號。

**其他值得關注的預測：**
- **亞斯伯格症候群**屬於自閉症譜系，而 risperidone 本已用於自閉症相關易怒。這主要與既有適應症重疊，不算真正的新適應症，也不應視為新增的再利用證據。
- **Phelan-McDermid 症候群**（SHANK3 單倍不足）常合併自閉症樣表現、易怒與攻擊行為，這些症狀正是 risperidone 在一般自閉症中已有效益的範圍。目前僅有斑馬魚模型的前臨床研究作為間接支持，且屬症狀層面而非疾病修飾。
- **毛髮拔除症**被視為強迫症譜系疾病，多巴胺與血清素失調被認為與其有關。Risperidone 的 D2 阻斷加 5-HT2A 拮抗，理論上可作為 SSRI 的增效治療，與其在難治型強迫症的用法類似。
- **釉質-腦-少汗症候群**（Kohlschütter-Tönz 症候群，ROGDI 相關）無已知機轉關聯。因部分抗精神病藥可能降低癲癇閾值，此項還有安全疑慮。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為證據最完整的預測（毛髮拔除症）之文獻，以及 Phelan-McDermid 症候群的前臨床研究。排名第 1 項無任何文獻。

**毛髮拔除症**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38797877](https://pubmed.ncbi.nlm.nih.gov/38797877/) | 2025 | Review | Int J Dermatol | 毛髮拔除症缺乏治療指引，藥物治療選擇複雜，探討是否需要更好的醫師教育 |
| [9108814](https://pubmed.ncbi.nlm.nih.gov/9108814/) | 1997 | 病例系列／開放標籤 | J Clin Psychiatry | 以 risperidone 增強血清素再回收抑制劑，用於強迫症及相關疾病 |
| [10357517](https://pubmed.ncbi.nlm.nih.gov/10357517/) | 1999 | 病例系列 | J Child Adolesc Psychopharmacol | 3 名 SSRI 難治型患者加用 risperidone 0.5–3 mg/日，3 人症狀均明顯減輕 |
| [12297616](https://pubmed.ncbi.nlm.nih.gov/12297616/) | 2002 | 個案報告 | Psychosomatics | 難治型毛髮拔除症使用 risperidone |
| [11320684](https://pubmed.ncbi.nlm.nih.gov/11320684/) | 2001 | 個案報告 | Can J Psychiatry | 難治型個案以 risperidone 增強 fluvoxamine 治療 |
| [15034500](https://pubmed.ncbi.nlm.nih.gov/15034500/) | 2002 | 個案報告 | CNS Spectrums | 思覺失調症患者合併毛髮拔除症，以 risperidone 治療精神症狀，加 citalopram 後毛髮拔除症部分緩解 |
| [24598474](https://pubmed.ncbi.nlm.nih.gov/24598474/) | 2014 | 個案報告 | J Am Med Dir Assoc | 高齡個案使用 risperidone 合併 naltrexone 治療成功 |
| [34563228](https://pubmed.ncbi.nlm.nih.gov/34563228/) | 2021 | 個案報告 | Ann Gen Psychiatry | 毛髮拔除症合併暴食症，合併 N-乙醯半胱胺酸協同治療 |
| [23466108](https://pubmed.ncbi.nlm.nih.gov/23466108/) | 2013 | 世代／臨床概況（間接，妄想性寄生蟲症） | Asian J Psychiatry | 妄想性寄生蟲症的臨床特徵，與毛髮拔除症僅為間接相關 |

**Phelan-McDermid 症候群**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37868296](https://pubmed.ncbi.nlm.nih.gov/37868296/) | 2023 | 前臨床（斑馬魚模型） | F1000Research | 此症候群常用藥物對 shank3 斑馬魚的感覺行為有不同影響 |
| [35328058](https://pubmed.ncbi.nlm.nih.gov/35328058/) | 2022 | Review | Genes | Phelan-McDermid 症候群的臨床、遺傳特徵與跨領域處置 |

**證據解讀：** 毛髮拔除症的報告方向一致為正面，但皆屬個案或小型病例系列，存在發表偏差，且多數同時使用 SSRI、naltrexone 或 NAC，難以歸因於 risperidone 本身。目前沒有對照試驗。

---

## 香港上市資訊

香港共有 20 張有效許可證，皆為單一成分製劑，無已註銷。以下列出 5 張主要許可證（許可證資料未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50822 | RISPERDAL TAB 2MG（Johnson & Johnson） | 錠劑 | 資料未提供 |
| HK-50823 | RISPERDAL TAB 3MG（Johnson & Johnson） | 錠劑 | 資料未提供 |
| HK-51064 | RISPERDAL CONSTA FOR INJ 50MG (P/SYR)（Johnson & Johnson） | 長效注射劑 | 資料未提供 |
| HK-59970 | RISPERIDONE SANDOZ TAB 1MG（Sandoz） | 錠劑 | 資料未提供 |
| HK-64107 | RISPERIDONE ACTAVIS TABLETS 1MG（Teva） | 錠劑 | 資料未提供 |

其餘許可證由 Teva、Sandoz、Hind Wing、Trenton-Boma、Healthcare Pharmascience、Jean-Marie 等廠商持有，涵蓋 0.25 mg 至 4 mg 不同規格。

---

## 安全性考量

**知識圖譜標示的禁忌或需謹慎的疾病**（來自知識圖譜關聯，非仿單文字）：
- 心血管：心肌梗塞、冠狀動脈血栓、猝死性心搏停止、心臟傳導疾病、心臟病、中風、腦血管疾病、腦梗塞、低血壓、姿勢性低血壓、姿勢性直立心搏過速症候群、多系統萎縮
- 代謝：糖尿病、高血糖、糖尿病酮酸中毒、高脂血症、家族性高脂血症、肥胖
- 血液：嗜中性白血球減少、顆粒球缺乏症、血紅素病變
- 其他：癲癇、肝病、肝衰竭、膽囊疾病、女性乳癌

**藥物交互作用：** 共查得 100 筆，以下為部分範例。
- **重大 (Major)**：Bupropion、Morphine
- **中度 (Moderate)**：Acarbose、Famotidine、Epinephrine、Hydrocortisone、Metformin、Albiglutide、Alogliptin、Canagliflozin、Amphotericin B、Atropine、Hyoscyamine、Loperamide、Lorcaserin 等
- **輕微 (Minor)**：Ranitidine

其中降血糖藥物的交互作用，與 risperidone 可能升高血糖的風險相呼應。抗膽鹼藥物與其合併使用時也需留意。

**其他提醒：** 釉質-腦-少汗症候群的預測涉及癲癇，而 risperidone 可能降低癲癇閾值，需特別小心。對毛髮拔除症這類通常不危及生命的疾病，須審慎權衡代謝與錐體外症狀風險。

仿單中的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（排名第 1 項）；毛髮拔除症為 Research Question**

**理由：**
- 排名第 1 的預測（家族性水平凝視麻痺合併進行性脊柱側彎）分數高，但沒有機轉關聯、試驗或文獻，僅是模型預測，不建議推進。
- 毛髮拔除症有一致的個案層級正面報告與合理的 OCD 譜系機轉，值得作為研究問題，但缺乏對照試驗，且報告受發表偏差與合併治療干擾，證據不足以支持臨床推廣。

**若要推進需要：**
- 取得香港仿單的警語與禁忌資料（目前為阻擋性資料缺口，無法進入安全性篩選）
- 補齊 risperidone 的作用機轉資料
- 針對毛髮拔除症設計小型隨機對照試驗（SSRI 增效 vs. 安慰劑），並明確監測代謝指標與錐體外症狀
- 評估 Phelan-McDermid 症候群的症狀導向（易怒、攻擊）使用，並確認與既有自閉症適應症的差異
- 亞斯伯格症候群項目應視為與既有適應症重疊，不列為新的再利用證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

