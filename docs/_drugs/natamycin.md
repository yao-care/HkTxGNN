---
layout: default
title: Natamycin
parent: 高證據等級 (L1-L2)
nav_order: 516
evidence_level: L1
indication_count: 5
---

# Natamycin
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

# Natamycin：從真菌感染到外陰陰道念珠菌病

## 一句話總結

Natamycin（DB00826）是一種多烯類（polyene）大環內酯抗真菌藥，傳統上用於眼部、皮膚等淺表真菌感染的局部治療。
TxGNN 模型預測它對**外陰陰道念珠菌病 (Vulvovaginal Candidiasis)** 有效，
目前有 **1 個已完成的 Phase 3 臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 真菌感染（眼部角膜炎、皮膚/黏膜念珠菌病等淺表黴菌感染；香港未上市，無官方許可證文字可佐證） |
| 預測新適應症 | 外陰陰道念珠菌病 (Vulvovaginal Candidiasis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Natamycin 是多烯類大環內酯抗真菌藥，其機轉為與真菌細胞膜上的麥角固醇（ergosterol）結合，破壞膜完整性，對 Candida 屬真菌具有直接殺菌/抑菌作用。目前缺乏 DrugBank 詳細 MOA 資料查詢結果，上述機轉描述來自本次證據收集中對適應症關聯性的分析。

原適應症（淺表真菌感染，如角膜炎、皮膚念珠菌病）與新預測適應症（外陰陰道念珠菌病）的致病菌相同，皆為 Candida 屬感染，僅感染部位不同。機轉上並無跨越障礙，且國際上早已有實際臨床使用先例（Pimafucin 陰道栓劑），並非單純模型外推。

事實上，本次證據收集到的核心試驗（NCT06411314）即為 Natamycin 陰道栓劑治療外陰陰道念珠菌病的 Phase 3 RCT，且歷史文獻（最早可溯及 1960-1980 年代）已大量記載 Natamycin（Pimafucin/pimaricin）用於陰道念珠菌病的治療經驗，顯示這個「新適應症」實際上是一個已有長期臨床實作基礎、但缺乏當地（香港）法規認可的用途。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06411314](https://clinicaltrials.gov/study/NCT06411314) | Phase 3 | 完成 | 218 | 比較 Natamycin 100mg + Lactulose 300mg 陰道栓劑 vs. Pimafucin（單方 Natamycin）vs. 單方 Lactulose，評估合併劑型於非孕成年女性外陰陰道念珠菌病之優越療效與安全性 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39979898](https://pubmed.ncbi.nlm.nih.gov/39979898/) | 2025 | RCT | BMC Women's Health | Natamycin + Lactulose 陰道栓劑治療成年女性外陰陰道念珠菌病之療效與安全性評估 |
| [4561566](https://pubmed.ncbi.nlm.nih.gov/4561566/) | 1972 | Cohort | Med J Australia | Fungilin（amphotericin B）與 Pimafucin（natamycin）陰道栓劑治療陰道念珠菌病之比較試驗 |
| [6760652](https://pubmed.ncbi.nlm.nih.gov/6760652/) | 1982 | Cohort | Acta Obstet Gynecol Scand | Natamycin 治療陰道念珠菌病，含性伴侶同時治療效果評估（治癒率 94% vs 88%） |
| [1082689](https://pubmed.ncbi.nlm.nih.gov/1082689/) | 1975 | Cohort | Zentralblatt fur Gynakologie | 口服 metronidazole 併用陰道 Natamycin 治療泌尿生殖道混合感染，念珠菌治癒率 89% |
| [6767924](https://pubmed.ncbi.nlm.nih.gov/6767924/) | 1980 | Cohort | MMW | 含 Pimafucin 乳膏新劑型應用於陰道念珠菌混合感染治療 |
| [41412769](https://pubmed.ncbi.nlm.nih.gov/41412769/) | 2025 | Review | Ceska a Slovenska farmacie | 烏克蘭 Lviv 地區外陰陰道念珠菌病之管理現況調查 |
| [18288724](https://pubmed.ncbi.nlm.nih.gov/18288724/) | 2008 | Review | J Pharm Sci | Natamycin：γ-環糊精包合物之陰道黏膜黏附劑型開發與評估 |
| [6972554](https://pubmed.ncbi.nlm.nih.gov/6972554/) | 1981 | Review | Przeglad Dermatologiczny | 不同劑型 Natamycin 治療皮膚黏膜多發性念珠菌病之療效 |
| [11048415](https://pubmed.ncbi.nlm.nih.gov/11048415/) | 1999 | Review | Ceska Gynekologie | 慢性陰道念珠菌病之診斷與治療，比較 Natamycin 與 Clotrimazole |
| [4545913](https://pubmed.ncbi.nlm.nih.gov/4545913/) | 1972 | Review | Sbornik Ved Praci Lek Fak | 婦科念珠菌病與滴蟲病治療經驗 |

---

## 香港上市資訊

Natamycin 目前**未在香港上市**，查無許可證記錄（0 張許可證）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 注意：現有證據包標記 TFDA/香港仿單警語與禁忌症資料為 **Blocking** 等級缺口（DG001），此為進入下一階段安全性初評（S1）的必要前置條件。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
已有 1 個 Phase 3 RCT（n=218，已完成）直接針對 Natamycin 陰道栓劑治療外陰陰道念珠菌病，加上數十年國際臨床使用文獻佐證，機轉與適應症關聯明確；但香港尚未上市、且缺乏當地安全性仿單資料，須在補齊安全性資料前列為守門條件。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（Blocking，DG001）
- 查詢 DrugBank API 取得完整作用機轉資料（High，DG002）
- 評估香港藥品上市/引進之法規路徑（目前 0 張許可證）
- 釐清劑型與給藥途徑（陰道栓劑 vs. 現有眼用/皮膚劑型）是否需另行開發

> 補充：同一證據包中另列出 candidiasis（廣義）、vulvitis、vulvovaginitis（皆為 L2-L3，Research Question 等級）與 trichomonal vulvovaginitis（L4，機轉不匹配，建議 Hold）等關聯適應症，顯示 Natamycin 之預測價值集中於 Candida 病因之外陰陰道感染，不宜外推至非真菌病因（如滴蟲病）。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

