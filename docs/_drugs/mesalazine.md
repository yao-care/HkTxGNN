---
layout: default
title: Mesalazine
parent: 僅模型預測 (L5)
nav_order: 558
evidence_level: L5
indication_count: 5
---

# Mesalazine
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

# Mesalazine：從潰瘍性結腸炎到先天性毛髮稀少伴青少年黃斑部失養症

## 一句話總結

Mesalazine（5-ASA，美沙拉嗪）是一種消炎藥，在文獻中主要用於潰瘍性結腸炎等發炎性腸道疾病。
TxGNN 模型預測它可能對**先天性毛髮稀少伴青少年黃斑部失養症 (Congenital hypotrichosis with juvenile macular dystrophy)** 有效。
目前**沒有臨床試驗和文獻**支持，這只是模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明；文獻指出 5-ASA 用於潰瘍性結腸炎 |
| 預測新適應症 | 先天性毛髮稀少伴青少年黃斑部失養症 (Congenital hypotrichosis with juvenile macular dystrophy) |
| TxGNN 預測分數 | 99.65% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Mesalazine 是 5-ASA 類消炎藥，可能透過抑制 COX／脂氧合酶與活化 PPAR-γ 發揮消炎作用。它在發炎性腸道疾病中的療效已被廣泛使用，但這些機轉與預測的新適應症之間，目前找不到明確關聯。

預測的疾病是與 CDH3 基因相關的極罕見遺傳疾病，特徵是毛髮稀少合併黃斑部退化。它不以慢性發炎為主要病因，與 5-ASA 的消炎作用沒有已知連結。

因此，0.9965 的高分只是模型在知識圖譜上的推論，缺乏生物學或臨床佐證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 20 張許可證，以下列出 5 張主要許可證（許可證資料未載明劑型與核准適應症）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-63749 | SYN-MESALAZINE ENTERIC-COATED TABLETS 250MG | SYNCO (H.K.) LIMITED |
| HK-37044 | PENTASA SUPP 1G | FERRING PHARMACEUTICALS LTD |
| HK-65052 | SALOFALK GASTRO-RESISTANT PROLONGED-RELEASE GRANULES 1.5G | A. MENARINI HONG KONG LIMITED |
| HK-51119 | ASACOL ENEMA 4G/100ML | ASSOCIATED MEDICAL SUPPLIES CO LTD |
| HK-59673 | SALOFALK 250 SUPP 250MG | A. MENARINI HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。香港衛生署仿單的警語與禁忌資料尚未取得，藥物交互作用查詢也無結果。

## 結論與下一步

**決策：Hold**

**理由：**
此預測只有模型分數，沒有任何臨床試驗或文獻，也找不到機轉連結，證據等級為 L5。疾病極為罕見，且與 5-ASA 的消炎作用無關，不建議投入資源。

**若要推進需要：**
- 補齊 Mesalazine 的作用機轉資料（可查詢 DrugBank）。
- 取得香港衛生署仿單的警語與禁忌資料，這是進入安全性篩選的前提。
- 釐清 CDH3 相關疾病與 5-ASA 之間是否存在任何生物學連結。

**其他值得關注的預測方向：**
- **骨關節炎（排名 2，L4）：** 2024 年 *Nature Communications* 的前臨床研究指出，5-ASA 可能經由 OSCAR-PPARγ 途徑抑制骨關節炎。目前僅有前臨床與體外證據，尚無人體資料，可列為研究問題。
- **類風濕性關節炎（排名 3，L4，Hold）：** 臨床活性主要來自 sulfasalazine，且文獻指出活性成分較可能是 sulfapyridine，5-ASA 單獨使用僅有微弱效果。相關的 Phase 3 試驗（NCT02930343）測試的是 sulfasalazine 而非 mesalazine，且已提前終止，因此不能直接視為 mesalazine 的證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

