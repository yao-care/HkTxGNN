---
layout: default
title: Domperidone
parent: 僅模型預測 (L5)
nav_order: 286
evidence_level: L5
indication_count: 1
---

# Domperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Domperidone：從原適應症（許可證未載明）到腎因性抗利尿不適當症候群

## 一句話總結

Domperidone（多潘立酮）是一種周邊多巴胺 D2/D3 受體拮抗劑，在香港已有 20 張許可證。
TxGNN 模型預測它可能對**腎因性抗利尿不適當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效。
目前**沒有臨床試驗，也沒有文獻**支持，僅有模型預測，屬於證據等級 L5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 腎因性抗利尿不適當症候群 (NSIAD) |
| TxGNN 預測分數 | 99.08% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，且原適應症在本次資料中也未載明。根據已知資訊，Domperidone 是周邊多巴胺 D2/D3 受體拮抗劑。

NSIAD 由 AVPR2（血管加壓素 V2 受體）的功能獲得性突變引起。這種突變使腎臟持續回收水分，且不依賴血中的血管加壓素 (AVP)。Domperidone 並不作用於 V2 受體或其下游訊號。即使多巴胺系統會影響 AVP 的釋放，在不依賴 AVP 的疾病中也沒有意義。

因此，**現有資料找不到直接的機轉關聯**。0.991 的高分只是知識圖譜的預測結果（排名 14,528），可能反映的是圖譜中水分、電解質或低血鈉相關節點的鄰近性，而不是經過驗證的藥理依據。由於缺少 DrugBank 的 MOA 與適應症資料，也無法用權威資料交叉驗證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 20 張許可證，以下列出 5 張主要許可證。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-58627 | APO-DOMPERIDONE TAB 10MG（HIND WING CO LTD） | 未載明 | 未載明 |
| HK-64541 | DOSIN TABLETS 10MG（TOP HARVEST PHARMACEUTICALS COMPANY LIMITED） | 未載明 | 未載明 |
| HK-48289 | NIDOLIUM TAB 10MG（SUNTOL MEDICAL LIMITED） | 未載明 | 未載明 |
| HK-44630 | DOMPEON TAB 10MG（NEOCHEM PHARMACEUTICAL LABORATORIES LTD.） | 未載明 | 未載明 |
| HK-39789 | COSTI TAB 10MG（STAR MEDICAL SUPPLIES LTD） | 未載明 | 未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有任何臨床試驗或文獻。
- 目前的機轉分析顯示，Domperidone 的作用標的與 NSIAD 的致病機轉（V2 受體功能獲得性突變）沒有直接關聯。
- 安全性資料（仿單警語、禁忌）也尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語、禁忌症與核准適應症（此為阻擋性缺口）。
- 從 DrugBank 補充作用機轉 (MOA) 與原適應症資料。
- 查找 Domperidone 與 AVPR2 或水分平衡相關的前臨床或機轉研究，確認是否存在合理的生物學路徑。
- 若找不到機轉支持，建議將此預測視為圖譜雜訊，不再投入資源。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

