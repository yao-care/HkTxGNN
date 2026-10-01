---
layout: default
title: Alverine
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 9
---

# Alverine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Alverine：從平滑肌鬆弛劑到輕度慢性憂鬱（Dysthymic Disorder）

## 一句話總結

Alverine 在香港以膠囊劑型上市，屬於平滑肌鬆弛劑。
TxGNN 模型預測它可能對**輕度慢性憂鬱 (Dysthymic Disorder)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個預測，僅有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未提供適應症文字 |
| 預測新適應症 | 輕度慢性憂鬱 (Dysthymic Disorder) |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Alverine 是平滑肌鬆弛劑，但香港許可證未列出核准適應症，也無法確認其原始機轉，因此無法建立與輕度慢性憂鬱之間的機轉連結。

現有資料中，唯一可能的線索來自一項小鼠焦慮模型研究（PMID 25199966）。該研究顯示 alverine citrate 有類似抗焦慮的效果，可能與血清素（5-HT1A）系統有關。血清素系統也與憂鬱症有關，但這個推論完全是推測，資料中沒有任何直接證據。

99.83% 的分數只代表知識圖譜上的相近程度，不代表療效。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 其他預測適應症的證據概況

模型另外預測了 8 個適應症，其中只有少數有零星資料，且多屬間接證據。

| 排名 | 預測適應症 | 分數 | 證據等級 | 現有證據 |
|------|-----------|------|---------|---------|
| 2 | 神經症 (Neurotic Disorder) | 99.59% | L5 | 無 |
| 3 | 焦慮症 (Anxiety Disorder) | 99.45% | L4 | 小鼠焦慮模型研究 [25199966](https://pubmed.ncbi.nlm.nih.gov/25199966/)（2014，*Eur J Pharmacol*）顯示 alverine citrate 有類似抗焦慮的效果；另有 1 個腸躁症試驗 [NCT00934973](https://clinicaltrials.gov/study/NCT00934973)（Phase 4，已完成，135 人），但族群與終點是腸躁症，不能當作焦慮症證據 |
| 4 | 偏頭痛 (Migraine Disorder) | 99.25% | L5 | 無 |
| 5 | 神經質憂鬱 (Neurotic Depression) | 99.16% | L5 | 僅有 1 篇網絡藥物再定位的計算研究 [30087074](https://pubmed.ncbi.nlm.nih.gov/30087074/)（2018，*Eur Neuropsychopharmacol*），為預測性質，未確認 alverine 是否為其候選藥物 |
| 6 | 憂鬱症 (Melancholia) | 99.14% | L5 | 同上（PMID 30087074） |
| 7 | 嬰兒良性陣發性斜頸 | 99.07% | L5 | 無，推測為圖譜相近性造成，不具可行性 |
| 8 | 懼曠症 (Agoraphobia) | 99.06% | L5 | 無 |
| 9 | 先天性單一 ACTH 缺乏症 | 99.02% | L5 | 無，推測為圖譜假象，建議降低優先度 |

其中**焦慮症**是目前證據最多的方向，但仍屬前臨床階段，尚無人體資料。

## 香港上市資訊

許可證資料未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-26461 | SPASMONAL CAP 60MG | VIATRIS HEALTHCARE HONG KONG LIMITED |
| HK-54718 | ALMETIN SOFT CAP | LAFARGE CO., LIMITED |
| HK-35395 | METEOSPASMYL CAP | DCH AURIGA (HONG KONG) LIMITED - HEALTHCARE DIVISION |
| HK-62910 | AVARIN CAPSULES | ZUELLIG PHARMA LIMITED |
| HK-68438 | ALBISTA CAPSULES | LSB (HK) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（輕度慢性憂鬱）沒有任何臨床試驗或文獻，只有模型分數，證據等級為 L5。
- 香港仿單的警語與禁忌資料缺失，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語、禁忌症與適應症資料。
- 補齊 alverine 的作用機轉，並驗證 5-HT1A 結合等假設。
- 若要優先探索，可先從**焦慮症**切入：檢視既有腸躁症族群中的焦慮或情緒相關結果，再決定是否設計人體研究。
- 確認 PMID 30087074 是否真的將 alverine 列為候選藥物，以及是否有實驗驗證。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

