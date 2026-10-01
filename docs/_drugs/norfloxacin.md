---
layout: default
title: Norfloxacin
parent: 僅模型預測 (L5)
nav_order: 618
evidence_level: L5
indication_count: 5
---

# Norfloxacin
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

# Norfloxacin：從細菌感染到多株性高黏滯症候群

## 一句話總結

Norfloxacin 是氟喹諾酮類（fluoroquinolone）抗菌藥，原本用於細菌感染。
TxGNN 模型預測它可能對**多株性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome)** 有效，但目前**沒有臨床試驗，也沒有文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌感染（香港許可證未載明適應症文字，此為依藥物類別判斷） |
| 預測新適應症 | 多株性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome) |
| TxGNN 預測分數 | 99.70% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Norfloxacin 屬於氟喹諾酮類抗菌藥，一般認為它抑制細菌 DNA 旋轉酶（DNA gyrase）與拓樸異構酶 IV（topoisomerase IV），藉此殺菌。

多株性高黏滯症候群是免疫球蛋白多株性過量造成的血液黏滯度升高，與上述抗菌機轉**沒有已知關聯**。我們未找到合理的機轉連結。

0.997 的高分僅代表知識圖譜模型的推論，沒有任何試驗或文獻佐證，不應視為療效證據。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-41225 | APT-NORFLOXACIN CAP 200MG | APT PHARMA LIMITED |
| HK-41226 | APT-NORFLOXACIN CAP 100MG | APT PHARMA LIMITED |
| HK-50199 | MITATONIN OPHTHALMIC SOLUTION 0.3% | MAIN LIFE CORP LTD |
| HK-58792 | BAXICIN OPHTHALMIC SOLUTION 'S.T.' 3MG/ML | WAI LUN TRADING CO |
| HK-35834 | GYRABLOCK 400 TAB 400MG | STAR MEDICAL SUPPLIES LTD |

各許可證的劑型與核准適應症文字目前未收錄。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測只有模型分數，沒有試驗、文獻，也找不到合理的機轉連結（證據等級 L5）。
- 香港仿單的警語與禁忌尚未取得，無法進入安全性初篩。

**補充觀察：**
- 排名第 5 的預測「點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)」有 2 篇病例系列文獻（PMID 12867402、22959880），證據等級為 L4。
- 這兩篇的主題是微孢子蟲角膜結膜炎，標題未顯示 norfloxacin 是研究藥物。氟喹諾酮類也不是微孢子蟲的既定治療藥。
- 若要進一步探索，這個方向比首要預測更值得優先查證。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌與適應症資料。
- 補充詳細的作用機轉（MOA）資料，例如查詢 DrugBank。
- 查閱上述兩篇文獻全文，確認是否使用 norfloxacin 及其結果。
- 首要預測（多株性高黏滯症候群）若無新的機轉或臨床線索，不建議投入資源。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

