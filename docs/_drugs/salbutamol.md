---
layout: default
title: Salbutamol
parent: 僅模型預測 (L5)
nav_order: 797
evidence_level: L5
indication_count: 9
monitor_inn: "SALBUTAMOL"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "bronchitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
last_modified_at: 2026-10-23
description: "Salbutamol：預測新適應症為乳突狀結膜炎 (Papillary Conjunctivitis)（證據等級 L5）。原適應症：氣喘、支氣管疾病"
---

# Salbutamol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Salbutamol：從氣喘到乳突狀結膜炎
{: .text-alpha }

## 一句話總結

Salbutamol（沙丁胺醇）是 β2 腎上腺素受體促效劑，在知識圖譜中記錄的原適應症為氣喘與支氣管疾病。
TxGNN 模型預測它可能對**乳突狀結膜炎 (Papillary Conjunctivitis)** 有效，但目前針對此疾病**沒有任何臨床試驗或文獻**，僅有模型預測支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 氣喘、支氣管疾病（知識圖譜記錄的關聯；本次資料中的許可證未載明核准適應症文字） |
| 預測新適應症 | 乳突狀結膜炎 (Papillary Conjunctivitis) |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 核准數 | 至少 20 張（單一成分許可證，清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Salbutamol 為 β2 腎上腺素受體促效劑，在氣道平滑肌鬆弛上的作用已廣為人知。就一般藥理推論，β2 促效劑可能降低肥大細胞釋放介質，因而有可能減輕過敏性眼部發炎，但這只是推測。

乳突狀結膜炎屬眼表過敏／刺激性疾病，與氣喘同屬過敏相關疾病，這是兩者之間可能的關聯。不過，局部眼用 salbutamol 並非已確立的用法，本次資料中也沒有任何試驗或文獻直接研究此疾病。

整體而言，此預測目前僅是模型輸出，尚無實證支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

以下為資料中列出的前 5 張單一成分許可證（總數至少 20 張，清單可能不完整）。許可證資料中未載明核准適應症與劑型。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-34904 | VANTIN SYRUP 2MG/5ML | 未載明 | 未載明 |
| HK-02796 | VENTOLIN SOLN FOR I.V INFUSION 1MG/ML | 未載明 | 未載明 |
| HK-30060 | ASMALIN TAB 4MG | 未載明 | 未載明 |
| HK-53744 | AXCEL SALBUTAMOL-2 TAB 2MG | 未載明 | 未載明 |
| HK-35778 | VENTAMOL-2 TAB 2MG | 未載明 | 未載明 |

從品名可見，市面上有口服錠劑、糖漿、吸入劑與靜脈輸注液等多種劑型，但目前沒有眼用製劑的資料。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：高血壓、長 QT 症候群、癲癇、低鉀血症、糖尿病與糖尿病酮酸中毒、良性前列腺肥大、高眼壓、閉角型青光眼、代謝性酸中毒、心臟傳導疾病、甲狀腺機能亢進、膀胱頸阻塞、心肌缺血與冠狀動脈疾病等。
- **藥物交互作用**：共查詢到 100 筆，以下為部分範例。
  - 中度：Acarbose、Isometheptene、Famotidine、Epinephrine、Albiglutide、Alogliptin、Canagliflozin、Dapagliflozin、Clarithromycin、Cisapride。
  - 輕度：Hydrocortisone、Beclomethasone、Betamethasone、Budesonide、Dexamethasone。
- 若考慮眼部使用，知識圖譜顯示高眼壓與閉角型青光眼為相關禁忌，需特別留意。
- 文獻中亦有 salbutamol 或其賦形劑（如苯二甲烴銨）引起過敏反應的案例報告。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅有模型分數支持，沒有任何針對乳突狀結膜炎的試驗或文獻，證據等級為 L5。
- 局部眼用 salbutamol 並非已確立的用法，且知識圖譜顯示其與高眼壓、閉角型青光眼有禁忌關聯。

**若要推進需要：**
- 作用機轉資料，以及眼用給藥途徑的可行性評估
- 前臨床研究（如過敏性結膜炎動物模型）
- 眼部局部安全性評估，特別是眼壓影響
- 香港許可證與仿單的核准適應症、警語與禁忌症資料

---

**補充：其他候選適應症**

資料中同時列出其他預測，供後續評估參考，但皆不宜視為強力證據。

- **支氣管炎**（L3）：有 β2 促效劑用於慢性支氣管炎的文獻，但相關試驗多為毛細支氣管炎，是不同疾病。Cochrane 與網絡統合分析顯示支氣管擴張劑在毛細支氣管炎的臨床效益有限，疾病對應不精確。
- **過敏性休克**（L2）：有一項吸入 salbutamol 對照安慰劑的 Phase 3 RCT（[NCT05653024](https://clinicaltrials.gov/study/NCT05653024)），但針對的是食物過敏反應的腹痛，且僅收 24 人即提前終止，統計檢定力不足，不能視為強證據。Salbutamol 無法取代 epinephrine，最多作為輔助。
- **異位性結膜炎**（L4）：僅有動物前臨床研究（[PMID 3666475](https://pubmed.ncbi.nlm.nih.gov/3666475/)、[PMID 2906082](https://pubmed.ncbi.nlm.nih.gov/2906082/)），無人體試驗。
- **普通感冒**（L3）：有一篇比較蜂蜜、salbutamol 與安慰劑的隨機雙盲研究（[PMID 26859020](https://pubmed.ncbi.nlm.nih.gov/26859020/)），但設計與結果資料不足。
- **咽炎、鼻腔疾病、急性喉咽炎、肛門直腸狹窄**（L5）：無直接證據或機轉依據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

