---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 517
evidence_level: L5
indication_count: 1
---

# Levodopa
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

# Levodopa：從帕金森氏症到 Rasmussen 亞急性腦炎

## 一句話總結

Levodopa 是多巴胺前驅物，一般用於治療帕金森氏症。不過香港許可證資料並未載明核准適應症，這個說法是依藥理常識，不是資料庫內容。
TxGNN 模型預測它可能對 **Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis)** 有效。
目前**沒有臨床試驗**，也**沒有文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis) |
| TxGNN 預測分數 | 99.06% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 19 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，資料中也沒有原適應症。Levodopa 是多巴胺前驅物，用於補充多巴胺不足，多以複方形式上市，例如與 carbidopa 或 benserazide 合併。

Rasmussen 腦炎是罕見的慢性單側腦部發炎疾病，特徵是難治性局部癲癇和進行性半球功能缺損，一般認為與免疫機制有關。以現有資料，看不出多巴胺訊號與這種神經發炎或癲癇表現之間有已確立的機轉關聯。

TxGNN 的高分（0.99）只是知識圖譜預測。它可能反映的是藥物與疾病在神經相關基因或路徑節點上的網路鄰近性，不是經過驗證的疾病相關機轉。要說多巴胺訊號與此疾病有關，目前仍屬推測，需要獨立證據支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 19 張許可證，以下列出 5 張主要許可證。資料未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-43179 | APO-LEVOCARB TAB 100MG/25MG | HIND WING CO LTD |
| HK-30945 | MADOPAR HBS CAP "125" CONTROLLED RELEASE | ROCHE HONG KONG LIMITED |
| HK-15442 | MADOPAR '250' TAB | ROCHE HONG KONG LIMITED |
| HK-35055 | LEVOMED 100/25MG TAB | STAR MEDICAL SUPPLIES LTD |
| HK-42376 | APO-LEVOCARB TAB 250/25MG | HIND WING CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。藥物交互作用查詢未找到資料。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有臨床試驗、文獻或已知機轉支持，證據等級為 L5。
- 香港的仿單警語與禁忌資料也還沒取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單 PDF，補齊警語與禁忌症，才能進行安全性篩選
- 從 DrugBank 補充 Levodopa 的作用機轉（MOA）與原適應症
- 系統性檢索 PubMed 與臨床試驗登記，確認 Levodopa 或多巴胺相關藥物用於 Rasmussen 腦炎的任何報告
- 評估多巴胺訊號與神經免疫、癲癇機轉之間是否有可查證的連結
- 確認給藥途徑與疾病族群的相容性（目前尚未評估）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

