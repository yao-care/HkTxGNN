---
layout: default
title: Icatibant
parent: 高證據等級 (L1-L2)
nav_order: 384
evidence_level: L1
indication_count: 5
---

# Icatibant
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Icatibant：從（原適應症資料缺失）到 C1 Inhibitor Deficiency（C1 抑制物缺乏症）

## 一句話總結

Icatibant（DB06196）目前在台灣尚未上市，資料庫中也缺乏明確的原適應症與作用機轉紀錄。
TxGNN 模型預測它對 **C1 Inhibitor Deficiency（C1 抑制物缺乏症，即遺傳性血管性水腫 HAE）** 有效，
目前有 **23 個臨床試驗**和 **20 篇文獻**支持這個方向，證據等級達到最高的 L1。
需特別說明：這個「預測」其實對應到 icatibant 在國際上早已確立的核准適應症，並非全新機轉假說。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料庫未提供（見下方說明） |
| 預測新適應症 | C1 Inhibitor Deficiency（C1 抑制物缺乏症 / 遺傳性血管性水腫 HAE） |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1 |
| 台灣上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏正式登錄的作用機轉（MOA）資料。但從其他候選適應症的機轉分析文字中可交叉確認：icatibant 的藥理作用是**緩激肽 B2 受體拮抗劑（bradykinin B2 receptor antagonist）**。這與 C1 抑制物缺乏症（HAE）的病理機轉高度吻合——HAE 患者因 C1 抑制物（SERPING1）功能不足，無法有效抑制激肽釋放酶系統，導致緩激肽過量累積、微血管通透性增加而引發皮下與黏膜下水腫。阻斷下游 B2 受體正是針對此病理環節的直接治療策略。

更關鍵的是，本次證據蒐集到的臨床試驗與文獻，絕大多數並非「假設性」研究，而是**icatibant（原廠藥名 Firazyr）於各國核准後的關鍵性 RCT 與大規模上市後監測**（例如涵蓋 1,761 名受試者的 Icatibant Outcome Survey 登錄研究、日本上市後藥物使用調查等）。這代表 TxGNN 在知識圖譜上重新辨識出的，其實是這個藥物早已在國際間站穩腳步的核准適應症，只是台灣端的許可證與仿單資料尚未到位（見下方台灣上市資訊）。因此本案性質上更接近「藥物在地引進評估」，而非典型的機轉外推式老藥新用。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00097695](https://clinicaltrials.gov/study/NCT00097695) | Phase 3 | 完成 | 84 | 皮下注射 icatibant 治療 HAE 急性皮膚/腹部發作，安慰劑對照關鍵性試驗 |
| [NCT00912093](https://clinicaltrials.gov/study/NCT00912093) | Phase 3 | 完成 | 98 | icatibant vs 安慰劑治療 HAE 急性發作之 FAST-3 關鍵性 RCT |
| [NCT00500656](https://clinicaltrials.gov/study/NCT00500656) | Phase 3 | 完成 | 85 | icatibant vs 口服 tranexamic acid，比較 HAE 症狀緩解時間（FAST-2） |
| [NCT00997204](https://clinicaltrials.gov/study/NCT00997204) | Phase 3 | 完成 | 151 | 病患自行皮下注射 icatibant 之安全性、便利性與療效評估 |
| [NCT01457430](https://clinicaltrials.gov/study/NCT01457430) | Phase 4 | 完成 | 19 | 自我注射 icatibant 與醫療院所注射之療效／安全性比較 |
| [NCT03888755](https://clinicaltrials.gov/study/NCT03888755) | Phase 3 | 完成 | 8 | 日本患者急性 HAE 發作使用 icatibant 之療效、藥動學與安全性 |
| [NCT04654351](https://clinicaltrials.gov/study/NCT04654351) | Phase 3 | 完成 | 2 | 日本兒童青少年 HAE 患者皮下注射 icatibant 之安全性與藥動學 |
| [NCT01386658](https://clinicaltrials.gov/study/NCT01386658) | Phase 3 | 完成 | 32 | 兒童青少年 HAE 患者單次皮下注射 icatibant 之藥動學與安全性 |
| [NCT01034969](https://clinicaltrials.gov/study/NCT01034969) | N/A（登錄研究） | 完成 | 1761 | Icatibant Outcome Survey (IOS)：大型前瞻性上市後安全性觀察登錄 |
| [NCT04057131](https://clinicaltrials.gov/study/NCT04057131) | N/A（上市後調查） | 完成 | 179 | 日本 FIRAZYR 上市後藥物使用調查，收集真實世界安全性與療效資料 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24925394](https://pubmed.ncbi.nlm.nih.gov/24925394/) | 2014 | Review | Chemical Immunology and Allergy | 闡述緩激肽媒介疾病之機轉，含 C1 抑制物缺乏症病理生理 |
| [28687105](https://pubmed.ncbi.nlm.nih.gov/28687105/) | 2017 | Review | Immunology and Allergy Clinics of North America | 後天性 C1 抑制物缺乏症之診斷定義與分類 |
| [29757016](https://pubmed.ncbi.nlm.nih.gov/29757016/) | 2018 | Review | Expert Review of Clinical Immunology | Icatibant 用於兒童與青少年 HAE 治療之療效與安全性回顧 |
| [21284353](https://pubmed.ncbi.nlm.nih.gov/21284353/) | 2010 | Review | Prescrire International | Icatibant 治療 HAE 發作之獨立藥物評論 |
| [26106828](https://pubmed.ncbi.nlm.nih.gov/26106828/) | 2015 | Review | Current Opinion in Allergy and Clinical Immunology | 義大利 HAE 診斷與治療經驗回顧 |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | The Journal of Allergy and Clinical Immunology | 亞太地區 HAE（C1 抑制物缺乏症）疾病負擔回顧 |
| [31690390](https://pubmed.ncbi.nlm.nih.gov/31690390/) | 2019 | Review | Allergy and Asthma Proceedings | 遺傳性與後天性血管性水腫之總覽 |
| [28284781](https://pubmed.ncbi.nlm.nih.gov/28284781/) | 2017 | Review | JACI In Practice | 後天性 C1 抑制物缺乏症之診斷與病程管理 |
| [32753245](https://pubmed.ncbi.nlm.nih.gov/32753245/) | 2020 | Guideline/Review | La Revue de Médecine Interne | 法國 CREAK 對後天性 C1 抑制物缺乏症之診療建議 |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Systematic Review | Pneumonologia i Alergologia Polska | 系統性回顧比較 conestat alfa、C1INH 與 icatibant 治療成人 HAE 急性發作 |

---

## 台灣上市資訊

目前查無台灣藥品許可證資料，Icatibant 尚未於台灣上市（許可證數：0 張）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：本案在資料蒐集階段已標記一項 **Blocking 等級資料缺口**（TFDA 仿單警語/禁忌），此缺口導致目前無法進入 S1 安全性初評，詳見下方結論。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 已有多個完成之 Phase 3 關鍵性 RCT（NCT00097695、NCT00912093、NCT00500656 等）及大型上市後登錄研究（IOS 登錄 N=1761、日本上市後調查 N=179）支持 icatibant 對 C1 抑制物缺乏症（HAE）之療效與安全性，證據等級達 **L1**。
- 但台灣尚未上市（0 張許可證），且欠缺 TFDA 仿單警語/禁忌資料（Blocking 等級缺口），依規則無法進入 S1 安全性初評，故暫列 Hold，而非直接 Go。
- 此預測本質上是辨識出 icatibant 已在國際間確立的核准適應症，屬於「在地引進評估」而非機轉外推式的老藥新用假說。

**若要推進需要：**
- 取得 TFDA 或原廠仿單之警語、禁忌資料，完成 S1 安全性初評（Blocking 缺口）
- 補齊正式的藥物作用機轉（MOA）文獻佐證（High 缺口）
- 評估台灣上市或專案進口之法規途徑
- 其餘 4 個低分候選適應症（serpinopathy、pseudo-von Willebrand disease、primary release disorder of platelets、immune-mediated necrotizing myopathy）均為 L5、無臨床試驗或文獻支持，機轉關聯薄弱，暫不建議投入資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

