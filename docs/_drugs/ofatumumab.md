---
layout: default
title: Ofatumumab
parent: 高證據等級 (L1-L2)
nav_order: 538
evidence_level: L2
indication_count: 5
---

# Ofatumumab
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Ofatumumab：從慢性淋巴球性白血病到濾泡性淋巴瘤

## 一句話總結

Ofatumumab 是全人源抗 CD20 單株抗體，原本核准用於慢性淋巴球性白血病/小淋巴球性淋巴瘤（CLL/SLL）。
TxGNN 模型預測它對**濾泡性淋巴瘤 (Follicular Lymphoma)** 也可能有效，
目前有 **15 個臨床試驗**和 **20 篇文獻**支持這個方向。

（同一 Evidence Pack 中另有 4 個 CLL/SLL 相關亞型/驗證性預測，證據強弱不一，詳見文末「結論與下一步」。）

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性淋巴球性白血病/小淋巴球性淋巴瘤 (CLL/SLL)，Ofatumumab 之核准核心適應症 |
| 預測新適應症 | 濾泡性淋巴瘤 (Follicular Lymphoma) |
| TxGNN 預測分數 | 99.70% |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

正式 MOA 欄位目前缺乏記錄，但根據臨床試驗與文獻佐證，Ofatumumab 是全人源 IgG1κ 抗 CD20 單株抗體，結合 CD20 分子上獨特的短環表位，主要透過補體依賴性細胞毒殺作用 (CDC) 與抗體依賴性細胞毒殺作用 (ADCC) 清除 CD20 陽性 B 細胞。

CLL/SLL 與濾泡性淋巴瘤同屬 CD20 陽性 B 細胞淋巴增生性疾病，病理生理與細胞表面標記高度重疊。臨床上，Ofatumumab 常作為 rituximab 難治或復發後的替代抗 CD20 治療選項，多項試驗也將其用於 FL 病人（單藥、併 bendamustine、併 CHOP 等方案）。

機轉上，只要腫瘤細胞持續表現 CD20，Ofatumumab 的細胞毒殺機制便可外推適用；FL 的細胞來源（濾泡中心 B 細胞）與 CLL/SLL（周邊 B 細胞）雖不同，但 CD20 標靶生物學一致，這是 TxGNN 預測合理性的核心依據。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01077518](https://clinicaltrials.gov/study/NCT01077518) | Phase 3 | 提前終止 | 346 | Ofatumumab+bendamustine 併用 vs bendamustine 單藥治療 rituximab 難治之惰性 B-NHL；最高證據等級試驗，惟提前終止需留意解讀限制 |
| [NCT01286272](https://clinicaltrials.gov/study/NCT01286272) | Phase 2（隨機） | 完成 | 135 | 未治療 FL：ofatumumab+bendamustine ± bortezomib 直接比較 |
| [NCT00494780](https://clinicaltrials.gov/study/NCT00494780) | Phase 2（隨機） | 完成 | 59 | 未治療 FL：ofatumumab 兩種劑量併 CHOP 之劑量反應設計 |
| [NCT00394836](https://clinicaltrials.gov/study/NCT00394836) | Phase 2 | 完成 | 116 | Rituximab 難治 FL 病人單用或併化療之單臂國際多中心試驗 |
| [NCT01190449](https://clinicaltrials.gov/study/NCT01190449) | Phase 2 | 完成 | 51 | 未治療 stage II-IV FL 之 ofatumumab 單藥療效 |
| [NCT02710643](https://clinicaltrials.gov/study/NCT02710643) | Phase 2 | 完成 | 110 | Stage I/II FL：局部放療併/未併 ofatumumab，依 Bcl-2 分子分層追蹤 |
| [NCT00823719](https://clinicaltrials.gov/study/NCT00823719) | Phase 2 | 完成 | 61 | Ofatumumab 併 ICE 或 DHAP 化療用於復發/難治侵襲性淋巴瘤，移植前橋接治療 |
| [NCT01294579](https://clinicaltrials.gov/study/NCT01294579) | Phase 2 | 完成 | 49 | Rituximab 治療後復發之惰性 B-NHL（含 FL）：ofatumumab+bendamustine 併維持治療 |
| [NCT01239394](https://clinicaltrials.gov/study/NCT01239394) | Phase 2 | 完成 | 43 | 未治療惰性 B 細胞淋巴瘤初始全身性治療之 ofatumumab 療效與安全性 |
| [NCT00742144](https://clinicaltrials.gov/study/NCT00742144) | Phase 1 | 完成 | 6 | 日本族群 FL/CLL 病人 ofatumumab 單藥安全性、耐受性與 PK 資料 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31174236](https://pubmed.ncbi.nlm.nih.gov/31174236/) | 2019 | RCT | Cancer | CALGB 50904：高風險未治療 FL，ofatumumab+bendamustine ± bortezomib 隨機比較完全反應率與安全性 |
| [38937025](https://pubmed.ncbi.nlm.nih.gov/38937025/) | 2024 | Cohort/前瞻性試驗 | Lancet Haematology | FIL MIRO 最終結果：早期 FL 局部放療併 MRD 導向抗 CD20 免疫治療 |
| [22389254](https://pubmed.ncbi.nlm.nih.gov/22389254/) | 2012 | Cohort（多中心） | Blood | Rituximab 難治 FL：ofatumumab 單藥治療，整體反應率 13% |
| [22409295](https://pubmed.ncbi.nlm.nih.gov/22409295/) | 2012 | Phase 2 | British Journal of Haematology | 未治療 FL：ofatumumab 兩劑量併 CHOP 化學免疫治療 |
| [30723894](https://pubmed.ncbi.nlm.nih.gov/30723894/) | 2019 | Phase 2 單臂 | British Journal of Haematology | CALGB 50901：未治療低/中風險 FL 之 ofatumumab 單藥療效 |
| [18390837](https://pubmed.ncbi.nlm.nih.gov/18390837/) | 2008 | Phase 1/2 | Blood | Ofatumumab 首次於復發/難治 FL 之臨床應用結果 |
| [28983798](https://pubmed.ncbi.nlm.nih.gov/28983798/) | 2017 | Review | Advances in Therapy | 抗 CD20 抗體於 B 細胞血液腫瘤 20 年臨床經驗回顧，涵蓋 FL 治療地位 |
| [29934061](https://pubmed.ncbi.nlm.nih.gov/29934061/) | 2018 | 實證回顧 | Clinical Lymphoma, Myeloma & Leukemia | 抗 CD20 藥物於復發/難治 CLL、DLBCL、FL 之療效實證評估 |
| [26043777](https://pubmed.ncbi.nlm.nih.gov/26043777/) | 2015 | Review | Expert Opinion on Biological Therapy | Ofatumumab 於非何杰金氏淋巴瘤（含 FL）之治療角色回顧 |
| [21083037](https://pubmed.ncbi.nlm.nih.gov/21083037/) | 2010 | Review | Expert Review of Hematology | 濾泡性淋巴瘤新興治療策略，含抗 CD20 抗體選項 |

---

## 香港上市資訊

Ofatumumab 目前**未在香港上市**，無有效許可證紀錄，因此無法提供核准適應症文字。若要推進在地應用，需先確認藥物進口/註冊路徑。

---

## 細胞毒性

抗腫瘤藥物判定依據：Ofatumumab 為核准治療 CLL/SLL（血液惡性腫瘤）之單株抗體生物製劑，故納入本章節。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物 / 免疫治療（抗 CD20 單株抗體，非傳統細胞毒性化療藥物） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | CBC（含分類）、B 細胞計數、輸注反應相關生命徵象監測 |
| 處置防護 | 生物製劑靜脈輸注，需注意輸注反應（infusion reaction）防護與預投藥，非傳統細胞毒性藥物處置規範 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
濾泡性淋巴瘤此一預測適應症有多個 Phase 2/3 臨床試驗（含一項 Phase 3 RCT）及 20 篇文獻支持，且與 Ofatumumab 已核准的 CLL/SLL 適應症共享相同 CD20 標靶機轉，證據等級達 L2。惟香港尚未上市，且仿單安全性資料（DG001，Blocking）與正式 MOA 記錄（DG002）仍缺，須在補齊後才能進入下一階段安全性初評。

同一 Evidence Pack 中，CLL/SLL 本身（rank 5）證據等級達 L1，屬藥物既有核心適應症的驗證性結果，非新預測；其兩個 IGHV 分子亚型（pregerminal center、mutated/germinal center-like，rank 1-2）目前無亞型專屬試驗或文獻，僅列為 Research Question；「leukemia, lymphocytic, susceptibility to」（rank 4）經判定為本體論映射雜訊（非可治療疾病實體），建議 Hold，不予推進。

**若要推進需要：**
- 取得 Ofatumumab 官方仿單警語/禁忌症資料，解除 Blocking data gap（DG001）
- 向 DrugBank 查證並補齊正式 MOA 記錄（DG002）
- 評估香港藥物註冊/引進可行性（目前 0 張許可證）
- 持續追蹤 CLL/SLL 分子亞型（IGHV 突變狀態）之亞型層級證據，待資料成熟後重新評分
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

