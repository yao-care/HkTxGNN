---
layout: default
title: Isoflurane
parent: 僅模型預測 (L5)
nav_order: 486
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Isoflurane：預測新適應症為Prinzmetal 心絞痛 (Prinzmetal angina)（證據等級 L5）。原適應症：香港許可證資料未載明核准適應症（依藥物類別為吸入性全身麻醉）"
monitor_inn: "ISOFLURANE"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "manic bipolar affective disorder", "trichotillomania", "dysthymic disorder"]
---

# Isoflurane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Isoflurane：從麻醉用途到 Prinzmetal 心絞痛

## 一句話總結

Isoflurane 是一種吸入性揮發性麻醉劑，在香港已有 4 張有效許可證。
TxGNN 模型預測它可能對 **Prinzmetal 心絞痛 (Prinzmetal angina)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。
在其他四個預測適應症中，只有「躁型雙相情感障礙」有 3 篇間接文獻，而且都不足以支持療效。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症（依藥物類別為吸入性全身麻醉） |
| 預測新適應症 | Prinzmetal 心絞痛 (Prinzmetal angina) |
| TxGNN 預測分數 | 99.67% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Isoflurane 是揮發性吸入麻醉劑，對血管平滑肌有擴張作用（可降低細胞內鈣、調節 KATP 通道），理論上可能緩解冠狀動脈痙攣，而這正是 Prinzmetal 心絞痛的病理特徵。

不過這個推論仍屬推測。Isoflurane 在缺血性心臟病中曾有「冠狀動脈竊血」的爭議，而且它是只能在監測下給予的全身麻醉劑，不適合作為血管痙攣性疾病的長期治療。TxGNN 分數僅反映知識圖譜的關聯性，並非實際療效證據。

其他預測適應症如下，同樣都屬於推測：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 說明 |
|------|-----------|-----------|---------|------|
| 2 | Tourette 症候群 | 99.61% | L5 | 理論上 GABA-A 增強與 NMDA 抑制可能降低神經迴路過度興奮，但無任何研究，且不適合長期使用 |
| 3 | 躁型雙相情感障礙 | 99.57% | L4 | 僅有間接證據，見下方說明 |
| 4 | 拔毛症 | 99.54% | L5 | 無明確機轉依據，亦無研究 |
| 5 | 輕度慢性憂鬱症 | 99.27% | L5 | 麻醉劑與難治型憂鬱症的關聯僅屬推論，無資料支持 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

Prinzmetal 心絞痛目前無相關文獻。以下為排名第 3 的「躁型雙相情感障礙」所列出的 3 篇文獻，均為間接證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8462536](https://pubmed.ncbi.nlm.nih.gov/8462536/) | 1993 | 小型開放式研究 | European Journal of Anaesthesiology | 12 位嚴重憂鬱症患者的自身對照比較：爆發抑制式 Isoflurane 麻醉與電痙攣治療 (ECT) 後憂鬱症狀均明顯改善。針對的是憂鬱症而非躁症，且為非對照研究 |
| [7502646](https://pubmed.ncbi.nlm.nih.gov/7502646/) | 1995 | 病例報告 | AANA Journal | 一位有躁鬱症病史的患者於麻醉期間的惡性高熱鑑別診斷，與療效無關 |
| [18930636](https://pubmed.ncbi.nlm.nih.gov/18930636/) | 2008 | 動物研究 | Psychiatry Research | 以大鼠躁症模型進行 PET 腦部代謝成像，Isoflurane 僅用於動物麻醉，並非測試療效 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-58404 | TERRELL ISOFLURANE LIQUID FOR INHALATION | 吸入液 | 未載明 |
| HK-50284 | ATTANE (ISOFLURANE) LIQ FOR INHAL'N (VET) | 吸入液（獸用） | 未載明 |
| HK-51392 | I.S.O. INHALATION ANAESTHETIC LIQUID 1ML/ML (VET) | 吸入液（獸用） | 未載明 |
| HK-40926 | ISOFLURANE | 吸入液 | 未載明 |

其中 HK-50284 與 HK-51392 的品名標示為獸用 (VET)。

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物－疾病關聯資料，並非仿單原文）：肝臟疾病、膽囊疾病、低血壓性疾患、麻醉引起的惡性高熱、運動誘發的惡性高熱、Duchenne 肌肉失養症、Becker 肌肉失養症及一般肌肉失養症。
- **藥物交互作用**：共查得 38 筆。
  - 嚴重 (Major)：Epinephrine
  - 中度 (Moderate)：Morphine、Opium
  - 其餘如 Atropine、Hydrocortisone、Omeprazole、Ondansetron 等未標示等級

其他警語與正式禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都沒有臨床試驗登記，最高排名的 Prinzmetal 心絞痛也沒有任何文獻，僅為 L5 的模型預測。
- 吸入性全身麻醉劑的給藥方式與風險，不適合用於 Prinzmetal 心絞痛等需要長期治療的疾病；且圖譜顯示低血壓性疾患與肝臟疾病為禁忌。

**若要推進需要：**
- 取得 Isoflurane 的作用機轉資料（MOA）與香港仿單的警語及禁忌症。
- 針對血管痙攣的前臨床研究，並評估冠狀動脈竊血的風險。
- 若要探索精神科方向，需進一步檢視爆發抑制式麻醉用於憂鬱症的對照研究，並評估給藥途徑是否可行。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

