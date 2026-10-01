---
layout: default
title: Terlipressin
parent: 僅模型預測 (L5)
nav_order: 851
evidence_level: L5
indication_count: 10
---

# Terlipressin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Terlipressin：從門脈高壓相關併發症到開角型青光眼（預測）

## 一句話總結

Terlipressin 是血管加壓素（vasopressin）類似物，臨床上主要用於肝硬化的門脈高壓相關併發症（如食道靜脈曲張出血、肝腎症候群）。
TxGNN 預測分數最高的新適應症是**開角型青光眼 (open-angle glaucoma)**，但目前**沒有任何臨床試驗或文獻**支持，機轉上也找不到合理依據，很可能是知識圖譜鄰近性造成的假訊號。
10 個預測中，唯一有實質證據的是**肺高壓 (pulmonary hypertension)**（排名第 3，約 20 篇相關文獻，屬 L3）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未登載適應症文字（本資料包的相關試驗多為肝硬化門脈高壓、肝腎症候群） |
| 預測新適應症 | 開角型青光眼 (open-angle glaucoma) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Terlipressin 是 V1a 血管加壓素受體促效劑的前驅藥，對內臟血管有較強的收縮作用。**開角型青光眼的預測在機轉上並不合理**：目前沒有已知機制能讓它降低眼壓。全身性血管收縮理論上還可能減少眼部灌流，因此不能排除有害的可能。

TxGNN 分數很高（99.78%），但這更可能反映知識圖譜中的鄰近關係，而不是藥理作用。第 2、6、9 名同樣是青光眼相關項目，與第 1 名高度重疊，應視為同一個圖譜假訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 其他預測適應症：肺高壓（排名第 3，唯一有證據者）

TxGNN 分數 99.56%，證據等級 **L3**，系統建議為「研究問題 (Research Question)」。

**機轉依據：** Terlipressin 偏向收縮內臟血管。已有小型人體血行動力學研究顯示，肝硬化合併門脈肺高壓的病人肺動脈壓下降，新生兒也有難治性肺高壓的救援性使用個案。但效果並不一致：血管加壓素類似物可能升高或降低肺血管阻力，取決於臨床情境。證據多來自肝硬化與門脈高壓族群，不一定能推廣到其他類型的肺高壓。

**相關臨床試驗（皆為間接證據，相關性 C 級）：**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03584087](https://clinicaltrials.gov/study/NCT03584087) | Phase 4 | 完成 | 74 | 食道靜脈曲張出血內視鏡結紮後的 terlipressin 治療；族群為門脈高壓，非肺高壓 |
| [NCT06027970](https://clinicaltrials.gov/study/NCT06027970) | Phase 3 | 未知 | 165 | 結紮後持續使用 terlipressin，終點為再出血，僅可參考肝硬化安全性 |
| [NCT05315557](https://clinicaltrials.gov/study/NCT05315557) | NA | 未知 | 100 | 肝硬化敗血性休克中，血管加壓素與 terlipressin 作為第二線升壓藥的比較 |
| [NCT06256432](https://clinicaltrials.gov/study/NCT06256432) | Phase 2 | 招募中 | 54 | Ambrisentan 用於肝腎症候群，與 terlipressin 治療肺高壓無直接關係 |

**相關文獻（挑選）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22893473](https://pubmed.ncbi.nlm.nih.gov/22893473/) | 2012 | 血行動力學研究 | Hepatobiliary Pancreat Dis Int | 肝硬化合併肺高壓者首劑 2 mg terlipressin 可降低肺血管阻力 |
| [21733953](https://pubmed.ncbi.nlm.nih.gov/21733953/) | 2012 | 血行動力學研究（超音波） | Angiology | 比較肝硬化有無肺高壓者，terlipressin 對肺與全身血行動力學的作用不同 |
| [15259082](https://pubmed.ncbi.nlm.nih.gov/15259082/) | 2004 | 臨床研究 | World J Gastroenterol | 以心臟超音波評估 terlipressin 對肝硬化病人收縮期肺動脈壓的影響 |
| [30971593](https://pubmed.ncbi.nlm.nih.gov/30971593/) | 2019 | 比較性臨床研究 | Ann Card Anaesth | 心臟手術合併肺高壓者，比較 terlipressin 與 norepinephrine 對抗 milrinone 誘發的低血壓 |
| [18280605](https://pubmed.ncbi.nlm.nih.gov/18280605/) | 2008 | 病例報告 | J Hepatol | 門脈肺高壓病人使用 terlipressin 一週後，肺動脈壓明顯下降 |
| [21292065](https://pubmed.ncbi.nlm.nih.gov/21292065/) | 2011 | 病例報告 | J Pediatr Surg | 先天性橫膈疝氣新生兒的難治性肺高壓，以 terlipressin 作救援治療 |
| [32999121](https://pubmed.ncbi.nlm.nih.gov/32999121/) | 2020 | 病例報告 | Indian Pediatr | 早產兒持續性肺高壓合併難治性休克的救援治療 |
| [19624374](https://pubmed.ncbi.nlm.nih.gov/19624374/) | 2009 | 臨床報告 | Paediatr Anaesth | Terlipressin 在先天性橫膈疝氣嚴重肺高壓處置中的角色 |

## 香港上市資訊

資料包列出 6 張許可證，其中 5 張有明細。劑型與核准適應症在登記資料中皆為空白。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61791 | GLYPRESSIN SOLUTION FOR INJECTION 1MG/8.5ML（Ferring） | 未登載（注射液） | 未登載 |
| HK-66714 | TERLIPRESSIN ACETATE EVER PHARMA SOLUTION FOR INJECTION 1MG/5ML | 未登載（注射液） | 未登載 |
| HK-66715 | TERLIPRESSIN ACETATE EVER PHARMA SOLUTION FOR INJECTION 2MG/10ML | 未登載（注射液） | 未登載 |
| HK-68775 | TERLIPRESSIN AFT SOLUTION FOR INJECTION 1MG/8.5ML | 未登載（注射液） | 未登載 |
| HK-68823 | TERLIPRESSIN ACETATE ALTAN SOLUTION FOR INJECTION 1MG/8.5ML | 未登載（注射液） | 未登載 |

## 安全性考量

- **已知不良反應：** 頭痛是 terlipressin 已知的不良反應。第 7 名「頭痛疾患」的預測很可能反映不良事件共現，而非治療效果。
- **心血管影響：** 文獻指出 terlipressin 會降低心輸出量（PMID 31841026）。
- **使用於肺高壓前須先評估：** 缺血、低血氧與體液過載。

藥物交互作用查詢無結果。其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第 1 的開角型青光眼沒有任何臨床或文獻證據，機轉上也不合理，且有血管收縮可能減少眼部灌流的潛在風險，不建議推進。
- 其他青光眼、斜視、甲狀腺機能亢進、三叉自主神經性頭痛等預測同屬 L5，同樣建議暫緩。
- 若要保留一個研究方向，肺高壓（L3）是唯一值得追蹤的，建議列為研究問題。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症（目前缺漏，屬阻斷性缺口）
- 補齊作用機轉資料（DrugBank）
- 肺高壓方向：做系統性文獻回顧，區分門脈肺高壓與其他類型，並評估肺血管阻力升降不一致的風險
- 針對缺血、低血氧與體液過載擬定安全性監測計畫

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

