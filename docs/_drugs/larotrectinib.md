---
layout: default
title: Larotrectinib
parent: 中證據等級 (L3-L4)
nav_order: 503
evidence_level: L4
indication_count: 10
---

# Larotrectinib
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Larotrectinib：從 NTRK 融合陽性實體腫瘤到多發性內分泌腫瘤

## 一句話總結

Larotrectinib 是選擇性 TRK（NTRK1/2/3）抑制劑，原本用於治療 NTRK 基因融合陽性的實體腫瘤。
TxGNN 模型預測它可能對**多發性內分泌腫瘤 (Multiple Endocrine Neoplasia, MEN)** 有效，但目前只有 **1 個間接相關的臨床試驗**和 **2 篇間接相關的文獻**，且都不是直接研究 larotrectinib 用於 MEN，證據薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | NTRK 基因融合陽性實體腫瘤（香港許可證未載明適應症文字，此處依證據包的機轉說明） |
| 預測新適應症 | 多發性內分泌腫瘤 (Multiple Endocrine Neoplasia) |
| TxGNN 預測分數 | 99.24% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Larotrectinib 是選擇性 TRK（NTRK1/2/3）抑制劑。目前缺乏詳細的作用機轉資料庫記錄，以上描述來自證據包的機轉說明。它的療效建立在腫瘤帶有 NTRK 融合這項生物標記上，與腫瘤長在哪個器官無關。

MEN，特別是 MEN2，主要由 **RET** 基因突變驅動，並常伴隨甲狀腺髓樣癌。Larotrectinib **不作用於 RET**，因此這個預測的機轉連結是間接的。它只來自兩個方向：一是激酶抑制劑在 RET 驅動的內分泌腫瘤中的治療經驗，二是甲狀腺癌中罕見的 NTRK 融合。

所以，TxGNN 的高分**沒有得到 TRK 特異性機轉的支持**。若 MEN 患者的腫瘤剛好帶有 NTRK 融合，才有理由使用 larotrectinib，此時依據是融合標記，不是 MEN 這個診斷。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | 進行中（不再招募） | 6452 | NCI-MATCH：依基因檢測結果分派治療的泛癌種試驗，對象為晚期難治性實體腫瘤、淋巴瘤或多發性骨髓瘤。並非針對 MEN，也非隨機分派；是否受益取決於有無 NTRK 融合。 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | 回顧晚期甲狀腺癌的標靶治療。核准藥物多為抗血管新生的多標靶激酶抑制劑，也有針對特定突變的適應症。未專門探討 larotrectinib。 |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | 前臨床／個案 | NPJ Precision Oncology | 一名 RET 突變的轉移性甲狀腺髓樣癌患者接受 selpercatinib 後，出現由其他致癌基因引起的抗藥性。與 larotrectinib 無直接關係。 |

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66491 | VITRAKVI CAPSULES 100MG | BAYER HEALTHCARE LIMITED |
| HK-66492 | VITRAKVI CAPSULES 25MG | BAYER HEALTHCARE LIMITED |
| HK-66493 | VITRAKVI ORAL SOLUTION 20MG/ML | BAYER HEALTHCARE LIMITED |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（TRK 抑制劑），非傳統細胞毒性化療藥物 |

其他細胞毒性相關項目（骨髓抑制風險、致吐性分級、監測項目、處置防護）請參考原廠仿單的警語與注意事項。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數雖高（99.24%），但 larotrectinib 不作用於 MEN 的主要驅動基因 RET，且沒有任何直接研究支持。
- 唯一的臨床試驗是泛癌種的 NCI-MATCH，2 篇文獻也都不是研究 larotrectinib。香港仿單的警語與禁忌資料尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症，這是目前的阻斷性缺口。
- 補充 DrugBank 的詳細作用機轉資料。
- 確認 MEN 患者中 NTRK 融合的實際盛行率，並搜尋 larotrectinib 用於 MEN 或甲狀腺髓樣癌的病例報告或試驗。
- 若走標記導向的路線，改以「NTRK 融合陽性」作為適用條件，而不是以 MEN 為整體適應症。
- 其他預測中，「孕激素受體陰性乳癌」（排名 6）有已完成的 Phase 2 試驗 NCT02576431（215 人，NTRK 融合實體腫瘤）。但該試驗不專屬乳癌，效益僅限融合陽性患者，同樣適合走標記導向的評估。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

