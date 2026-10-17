---
layout: default
title: Acemetacin
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Acemetacin：預測新適應症為骨關節炎易感性 (Osteoarthritis Susceptibility)（證據等級 L5）。原適應症：僵直性脊椎炎、風濕性疾病、纖維肌痛"
monitor_inn: "ACEMETACIN"
predicted_indications: ["osteoarthritis susceptibility"]
---

# Acemetacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Acemetacin：從僵直性脊椎炎等風濕性疾病到骨關節炎易感性

## 一句話總結

Acemetacin 是一種非類固醇抗發炎藥（NSAID），原本用於僵直性脊椎炎、風濕性疾病與纖維肌痛等相關適應症。
TxGNN 模型預測它可能對**骨關節炎易感性 (Osteoarthritis Susceptibility)** 有效，
但目前**沒有臨床試驗和文獻**支持這個方向，僅屬模型預測階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 僵直性脊椎炎、風濕性疾病、纖維肌痛（來自知識圖譜；香港許可證未列適應症文字） |
| 預測新適應症 | 骨關節炎易感性 (Osteoarthritis Susceptibility) |
| TxGNN 預測分數 | 99.22% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥理類別，Acemetacin 是 NSAID，也是 indomethacin 的前驅藥物（prodrug）。一般預期它會抑制 COX-1/COX-2，減少前列腺素介導的發炎與疼痛。這與骨關節炎的症狀緩解有合理的關聯。

不過有幾點需要留意。TxGNN 分數（99.22%）純粹是計算預測結果。「骨關節炎易感性」描述的是遺傳傾向，並不是可直接治療的臨床狀況，因此不太可能是真正的治療標的。這個高分較可能反映它在知識網路中與原適應症（僵直性脊椎炎、風濕性疾病）距離相近，而不是已驗證的機轉。

另外，Acemetacin 在部分國家已用於骨關節炎等肌肉骨骼疼痛的症狀治療，但本報告整理的資料並未包含這方面的佐證，需另行查證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-52308 | ACEMET CAP 60MG | 未提供 | 未提供 |
| HK-55919 | ACEMET RETARD CAP 90MG | 未提供 | 未提供 |

兩張許可證皆為單一成分製劑，狀態有效，持有者為 SYNMOSA BIOPHARMA (HONG KONG) COMPANY LIMITED。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅為 L5，只有模型預測，沒有任何臨床試驗或文獻佐證。
- 預測目標「骨關節炎易感性」是遺傳易感表型而非可治療的疾病，臨床上難以直接作為適應症，且作用機轉與安全性資料皆有缺口。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症。
- 補充 Acemetacin 的作用機轉資料（例如查詢 DrugBank）。
- 將預測目標改為可治療的臨床疾病（如症狀性骨關節炎），再檢索臨床試驗與文獻。
- 查證其他國家對骨關節炎的核准狀況，作為輔助證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

