---
layout: default
title: Nonivamide
parent: 僅模型預測 (L5)
nav_order: 615
evidence_level: L5
indication_count: 10
---

# Nonivamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Nonivamide：從外用止痛類製劑到肺動脈高壓

## 一句話總結

Nonivamide 是辣椒素（capsaicin）的類似物，在香港以外用液劑成分上市（如 Tiger Balm、Salonpas、Ammeltz 等產品），但許可證資料未登載核准適應症。
TxGNN 模型預測它可能對**肺動脈高壓 (Pulmonary Hypertension)** 有效，
目前**沒有臨床試驗，也沒有文獻**支持，僅有模型預測分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 肺動脈高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 99.81% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 12 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Nonivamide 是辣椒素類似物，也是 TRPV1 促效劑。TRPV1 表現於血管周圍的感覺神經，因此血管活性作用在理論上可想像。

不過，這個推論純屬推測。原適應症資料缺漏，也沒有任何試驗或文獻支持肺動脈高壓這個方向，分數高不等於機轉已被證實。

排名第 2 至第 10 的預測（都同樣沒有證據）大致分為三類：

| 類別 | 預測適應症 | 機轉合理性 |
|------|-----------|-----------|
| 血管類 | 周邊動脈疾病、周邊血管疾病、間歇性跛行 | 低至中。TRPV1 活化與 CGRP 釋放可能影響血管張力，但未經驗證 |
| 神經類 | 偏頭痛 | 相對最合理。TRPV1 促效劑可耗竭三叉神經感覺神經元的 CGRP 與 P 物質，辣椒素曾在頭痛情境被探索；nonivamide 是否適用尚無資料 |
| 心律不整類 | 心室頻脈、兒茶酚胺敏感性多形性心室頻脈 | 缺乏依據。心臟感覺傳入神經雖有 TRPV1，但對心律不整的影響未確立，甚至可能誘發心律不整 |
| 其他 | 急性淋巴母細胞白血病、脊柱後凸性心臟病、過敏性休克 | 無合理機轉，分數可能是知識圖譜的假象。Nonivamide 是感覺刺激物，可引發神經性發炎，對過敏性休克不太可能有益 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 12 張許可證，以下列出 5 張主要許可證（許可證資料未登載劑型與核准適應症）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66440 | TIGER BALM LOTION | Haw Par Brothers International (H.K.) Ltd |
| HK-66526 | NEW AMMELTZ YOKO YOKO EXTRA STRENGTH LIQUID | Kobayashi Pharmaceutical (Hong Kong) Company Limited |
| HK-62002 | SALONPAS LOTION | Hisamitsu Pharmaceutical (Hong Kong) Co., Limited |
| HK-00349 | AMMELTZ LOTION | Kobayashi Pharmaceutical (Hong Kong) Company Limited |
| HK-42348 | NEW AMMELTZ YOKO YOKO LIQUID | Kobayashi Pharmaceutical (Hong Kong) Company Limited |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型分數（L5），沒有任何臨床試驗或文獻佐證。
- 現有產品都是外用製劑，而肺動脈高壓等全身性疾病所需的給藥途徑尚未評估。心室頻脈等項目還有潛在的安全疑慮。

**若要推進需要：**
- 取得 DrugBank 的作用機轉資料，補上機轉連結分析。
- 下載並解析香港衛生署仿單，補齊警語、禁忌與核准適應症。
- 以 PubMed 與 ClinicalTrials.gov 檢索 nonivamide／capsaicin 相關研究，優先檢視偏頭痛與周邊血管疾病。
- 評估給藥途徑與現有外用劑型是否相容。
- 在完成上述工作之前，不建議進入安全性篩選階段。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

