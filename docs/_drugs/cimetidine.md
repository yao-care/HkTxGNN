---
layout: default
title: Cimetidine
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 4
monitor_inn: "CIMETIDINE"
predicted_indications: ["peptic ulcer perforation", "duodenal obstruction", "acne (disease)", "abnormality of glucagon secretion"]
last_modified_at: 2026-10-28
description: "Cimetidine：預測新適應症為消化性潰瘍穿孔 (peptic ulcer perforation)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Cimetidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Cimetidine：H2 受體拮抗劑 → 消化性潰瘍穿孔 (peptic ulcer perforation)
{: .text-alpha }

## 一句話總結

Cimetidine 是一種 H2 受體拮抗劑類的胃酸抑制藥物。
TxGNN 模型預測它可能對**消化性潰瘍穿孔 (peptic ulcer perforation)** 有效，
但目前**沒有臨床試驗**，且文獻多為病例報告與評論，其中不少反而描述「服用 cimetidine 期間仍發生穿孔」，並未顯示治療效益。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 消化性潰瘍穿孔 (peptic ulcer perforation) |
| TxGNN 預測分數 | 0.9977 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般認為 cimetidine 屬於 H2 受體拮抗劑，可抑制胃酸分泌，因此在消化性潰瘍的處置上有合理的輔助角色。

不過，穿孔是需要手術處理的急症，而非單靠抑制胃酸即可治療的疾病。現有文獻主要是病例報告與信件，描述在 cimetidine 治療期間或停藥後發生穿孔（PMID 3967139、6743974、922364），屬於安全性或治療失敗的訊號，而非療效證據。TxGNN 的高分可能反映的是它與消化性潰瘍疾病本身的關聯，而不是對穿孔的真正治療效果。

另有流行病學觀察（PMID 7082957）顯示 cimetidine 上市後，選擇性手術明顯減少（約 45%），但穿孔數僅下降約 10%，也無法證明 cimetidine 能治療或預防穿孔。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下依資料中的分類，列出與預測疾病較相關的文獻，皆為間接或低層級證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8364140](https://pubmed.ncbi.nlm.nih.gov/8364140/) | 1993 | 受控試驗回顧（維持治療） | Aliment Pharmacol Ther | H2 受體拮抗劑持續治療可降低潰瘍復發，但未直接探討穿孔 |
| [7082957](https://pubmed.ncbi.nlm.nih.gov/7082957/) | 1982 | 病例報告／信件 | Br J Surg | Cimetidine 上市後選擇性手術減少 45%，穿孔僅減少 10% |
| [6743974](https://pubmed.ncbi.nlm.nih.gov/6743974/) | 1984 | 病例報告 | Br J Surg | 9 例在 cimetidine 治療期間發生十二指腸潰瘍穿孔，皆需手術 |
| [3967139](https://pubmed.ncbi.nlm.nih.gov/3967139/) | 1985 | 病例報告 | Br J Surg | 描述服用 cimetidine 期間發生穿孔 |
| [6113521](https://pubmed.ncbi.nlm.nih.gov/6113521/) | 1981 | 評論 | Lancet | Cimetidine 與消化性潰瘍的評論 |
| [922364](https://pubmed.ncbi.nlm.nih.gov/922364/) | 1977 | 報告 | Br Med J | 停用 cimetidine 後發生消化性潰瘍穿孔 |

## 香港上市資訊

香港共有至少 20 張有效許可證，皆為單一成分製劑，以下為其中 5 張（清單可能不完整）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-41813 | TAMEDIN F C TAB 400MG | 未記載 | 未記載 |
| HK-47776 | ULCIMET 400 TAB 400MG | 未記載 | 未記載 |
| HK-38804 | STOMCAP-1 TAB 200MG | 未記載 | 未記載 |
| HK-65798 | SANWELL TABLETS 200MG | 未記載 | 未記載 |
| HK-63341 | SYNGAMET TABLET 200MG | 未記載 | 未記載 |

## 安全性考量

- **藥物交互作用**：已查詢到多項交互作用，其中中度者包括 Paclitaxel、Fentanyl、Acalabrutinib、Lidocaine、Acebutolol、Dihydrocodeine、Codeine、Tramadol、Nifedipine、Alfentanil；輕度者包括 Dolutegravir、Zidovudine、Acetaminophen、Ibuprofen 等。
- **臨床風險提示**：文獻顯示，cimetidine 治療期間或停藥後仍有穿孔個案，不應視為可預防或治療穿孔的藥物。

仿單的警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，也沒有直接研究 cimetidine 治療消化性潰瘍穿孔的文獻；現有資料多為病例報告，且偏向安全性或治療失敗訊號。穿孔屬於外科急症，不適合以抑酸藥作為主要療法。

**若要推進需要：**
- 設計針對穿孔後（含術後或非手術處置）輔助用藥的對照研究，與現行標準抑酸治療（如質子幫浦抑制劑）比較
- 取得完整作用機轉資料與香港仿單的警語、禁忌症
- 釐清 TxGNN 高分是否僅反映與一般消化性潰瘍的關聯
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

