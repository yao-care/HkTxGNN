---
layout: default
title: Nilotinib
parent: 僅模型預測 (L5)
nav_order: 609
evidence_level: L5
indication_count: 1
---

# Nilotinib
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

# Nilotinib：從 BCR-ABL 標靶抗癌藥到隆突性皮膚纖維肉瘤

## 一句話總結

Nilotinib 是一種多標靶酪胺酸激酶抑制劑，已在香港上市。
TxGNN 模型預測它可能對**隆突性皮膚纖維肉瘤 (Dermatofibrosarcoma protuberans, DFSP)** 有效，
但目前**沒有臨床試驗登記**，僅有 **1 篇**機轉層面的文獻回顧支持，屬於早期研究假說。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 隆突性皮膚纖維肉瘤 (Dermatofibrosarcoma protuberans) |
| TxGNN 預測分數 | 99.31% |
| 證據等級 | L4（僅有機轉層面的研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

DFSP 通常由 COL1A1-PDGFB 融合基因驅動，使 PDGFRB 受體持續被自體分泌活化，腫瘤因此不斷增生。Nilotinib 是多標靶酪胺酸激酶抑制劑，除了 BCR-ABL、KIT 和 DDR1，也能抑制 PDGFR。所以在機轉上，它有可能阻斷 DFSP 的關鍵驅動路徑。

同屬 PDGFR 抑制劑的 imatinib 已是 DFSP 的既定治療，這支持「抑制 PDGFR 對 DFSP 有效」的類別層級推論。TxGNN 給出 0.993 的高分，方向與此一致。

要注意的是，本次提供的資料中，作用機轉與原適應症欄位都缺漏，上述機轉是根據該藥與該疾病的一般知識推論，並非來自提供的藥品紀錄。資料也沒有包含 nilotinib 用於 DFSP 的專屬療效數據，因此目前只能說生物學上合理，尚未得到直接證實。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | 回顧小分子 PDGFR 抑制劑在腫瘤性疾病治療中的角色，屬機轉層面的背景證據，並非 nilotinib 用於 DFSP 的直接療效資料 |

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-56797 | TASIGNA CAP 200MG | Novartis Pharmaceuticals (HK) Limited |
| HK-60833 | TASIGNA CAP 150MG | Novartis Pharmaceuticals (HK) Limited |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（酪胺酸激酶抑制劑） |

其餘細胞毒性相關項目（骨髓抑制風險、致吐性、監測項目、處置防護）請參考原廠仿單的警語與注意事項。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測與一篇機轉層面的文獻回顧，沒有任何臨床試驗或 nilotinib 專屬的 DFSP 療效資料，證據停留在 L4。
- 香港仿單的警語與禁忌尚未取得，無法進入安全性初篩。

**若要推進需要：**
- 取得香港衞生署核准的仿單，解析警語、禁忌症和核准適應症（補上安全性缺口）。
- 從 DrugBank 補齊 nilotinib 的作用機轉資料。
- 搜尋 nilotinib 用於 DFSP 的專屬研究，例如病例報告、前臨床研究或早期臨床試驗，並與 imatinib 的既有證據比較。
- 確認 DFSP 患者是否具有 COL1A1-PDGFB 融合，作為潛在的病人篩選條件。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

