---
layout: default
title: Indomethacin
parent: 僅模型預測 (L5)
nav_order: 460
evidence_level: L5
indication_count: 5
---

# Indomethacin
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

# Indomethacin：從非選擇性 COX 抑制劑到短指併指症候群

## 一句話總結

Indomethacin（吲哚美辛）是非選擇性 COX-1/COX-2 抑制劑，透過阻斷前列腺素合成發揮消炎止痛作用。
TxGNN 模型預測它可能對**短指併指症候群 (Brachydactyly-Syndactyly Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 短指併指症候群 (Brachydactyly-Syndactyly Syndrome) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據已知資訊，Indomethacin 是非選擇性 COX 抑制劑，主要作用是阻斷前列腺素合成，用於消炎與止痛。

短指併指症候群是先天性肢體畸形，通常由發育相關基因變異造成，屬於結構性發育缺陷。消炎藥不預期能矯正這類缺陷，兩者之間**沒有已建立的機轉關聯**。

TxGNN 分數很高（99.97%，全體排名第 1093），但這來自知識圖譜的拓撲關係，沒有臨床或文獻佐證。因此不宜把高分視為療效證據。

同一批預測還包括以下四個罕見疾病，同樣沒有試驗或文獻，也沒有機轉關聯：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 |
|------|-----------|-----------|---------|
| 2 | 眼缺損小眼球-近端肢體發育不良症候群 (Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome) | 99.97% | L5 |
| 3 | 肢中發育不良，Hunter-Thompson 型 (Acromesomelic Dysplasia, Hunter-Thompson Type) | 99.89% | L5 |
| 4 | WHIM 症候群 (WHIM Syndrome) | 99.88% | L5 |
| 5 | 短體-牙釉質發育不全症候群 (Brachyolmia-Amelogenesis Imperfecta Syndrome) | 99.87% | L5 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張。資料中劑型與核准適應症欄位皆為空白。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67282 | TOSPAN INDOMETHACIN CAPSULES 25MG | WELLDONE PHARMACEUTICALS LIMITED |
| HK-67566 | KECENTIN CAPSULES 25MG | WELLDONE PHARMACEUTICALS LIMITED |
| HK-15122 | INDOMETHACIN CAP 25MG | NATIONAL PHARMACEUTICAL CO LTD |
| HK-67280 | EFORMAT INDOMETHACIN CAPSULES 25MG | WELLDONE PHARMACEUTICALS LIMITED |
| HK-21046 | INDOMETHACIN CAP 25MG | VICKMANS LABORATORIES LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型（L5），沒有臨床試驗或文獻。
- 適應症是先天性結構發育缺陷，與 COX 抑制之間沒有已知機轉關聯。
- 香港仿單的警語與禁忌資料尚缺，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衞生署仿單（警語、禁忌症、核准適應症），補齊安全性資料。
- 從 DrugBank 補上作用機轉資料。
- 找出前列腺素或 COX 相關路徑與該症候群病理之間的機轉證據，例如前臨床或動物模型研究。
- 檢索是否有相關病例報告或機轉研究；若仍完全沒有，建議不再投入資源。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

