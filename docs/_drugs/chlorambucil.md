---
layout: default
title: Chlorambucil
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 8
---

# Chlorambucil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Chlorambucil：從慢性淋巴性白血病到含 IGHV 體細胞超突變的 CLL/SLL 亞型

## 一句話總結

Chlorambucil 是一種氮芥類烷化劑，歷史上作為慢性淋巴性白血病（CLL）及低惡性度淋巴瘤的標準化療之一。TxGNN 模型預測它可能對 **IGHV 基因體細胞超突變型 CLL/SLL（CLL/SLL with IGHV somatic hypermutation）** 有效，預測分數高達 99.72%。目前針對此特定分子亞型尚無直接臨床試驗或文獻登記，但廣義 CLL 領域已有多項 Phase 3 試驗使用 Chlorambucil 作為對照組，間接支持其療效基礎。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性淋巴性白血病（CLL）及低惡性度淋巴瘤（依公開臨床資料；香港未有上市許可） |
| 預測新適應症 | IGHV 體細胞超突變型 CLL/SLL |
| TxGNN 預測分數 | 99.72% |
| 證據等級 | L5（此特定亞型）；廣義 CLL 具 L1 級間接證據 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前 DrugBank 作用機轉資料尚待補充（DG002）。依據已知藥理學知識，Chlorambucil 是氮芥（nitrogen mustard）衍生的**烷化劑**，透過與 DNA 鳥嘌呤形成共價交叉連結，阻斷 DNA 複製與轉錄，進而誘導腫瘤細胞凋亡。B 淋巴球（CLL 的腫瘤細胞）增殖相對緩慢，對烷化劑累積的 DNA 損傷尤為敏感，因此 Chlorambucil 長期作為 CLL 第一線化療的基準（comparator），並在多項大型 Phase 3 試驗中擔任對照組。

慢性淋巴性白血病按**免疫球蛋白重鏈可變區基因（IGHV）突變狀態**可分為兩大亞型：IGHV 突變型（本預測目標）病程相對緩慢、預後較佳；IGHV 未突變型進展較快、預後較差。TxGNN 預測 Chlorambucil 對 IGHV 突變型 CLL/SLL 有效，機轉上完全合理——此亞型腫瘤細胞增殖更為緩慢，對口服低強度烷化劑的耐受性通常較佳，且歷史上涵蓋兩種亞型患者的廣義 CLL 試驗均顯示 Chlorambucil 具一定療效。

值得注意的是，近年 ibrutinib（BTK 抑制劑）和 venetoclax（BCL-2 抑制劑）等標靶藥物在 CLL 的長期療效已優於 Chlorambucil（如 RESONATE-2 研究所示），導致其在現代 CLL 指引中的定位有所下降。然而在高齡、共病多、無法耐受強化療法的特定族群中，Chlorambucil 仍是可接受的輕度化療選項。

---

## 臨床試驗證據

目前針對「IGHV 體細胞超突變型 CLL/SLL」此特定亞型，**無直接臨床試驗登記**。

以下列出廣義 CLL 相關 Phase 3 試驗（Chlorambucil 作為研究藥物或對照組），提供間接佐證：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00046683](https://clinicaltrials.gov/study/NCT00046683) | Phase 3 | 完成 | 284 | Alemtuzumab vs Chlorambucil 作為進展性 B-CLL 第一線治療隨機比較試驗，Rai Stage I–IV 未曾治療患者 |
| [NCT00910910](https://clinicaltrials.gov/study/NCT00910910) | Phase 3 | 完成 | 450 | Lenalidomide vs Chlorambucil 用於老年未曾治療 B-CLL 患者（ORIGIN 研究），評估安全性與療效 |
| [NCT01905943](https://clinicaltrials.gov/study/NCT01905943) | Phase 3 | 完成 | 979 | Obinutuzumab 單獨或合併化療（含 Chlorambucil）治療未曾治療或復發/難治性 CLL 的 Post-Authorization 安全性研究 |

---

## 文獻證據

目前針對「IGHV 體細胞超突變型 CLL/SLL」此特定亞型，**無直接文獻**。

以下為從相關適應症中篩選出最具代表性的文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36672456](https://pubmed.ncbi.nlm.nih.gov/36672456/) | 2023 | Phase 3 長期追蹤 | Cancers | RESONATE-2：Ibrutinib vs Chlorambucil 在未曾治療 CLL/SLL（≥65 歲，無 del17p）患者的 ≥5 年追蹤，ibrutinib 療效顯著優於 Chlorambucil |
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Review | Ned Tijdschr Geneeskd | 概述 CLL 兩大亞型：IGHV 突變型（pre-germinal centre）與未突變型，其臨床表現、預後差異及治療策略 |
| [3307632](https://pubmed.ncbi.nlm.nih.gov/3307632/) | 1987 | Phase II | Cancer & Chemotherapy | Chlorambucil 在 8 名血液惡性腫瘤患者（含 5 名 CLL）的 Phase II 研究：2 名 CLL 及 1 名濾泡性淋巴瘤達部分緩解 |
| [3699123](https://pubmed.ncbi.nlm.nih.gov/3699123/) | 1986 | 個案報告 | Eur J Respir Dis | 49 歲男性原發性肺非何杰金淋巴瘤，Chlorambucil 治療 5 個月後達臨床緩解，後續放療鞏固 |
| [6248988](https://pubmed.ncbi.nlm.nih.gov/6248988/) | 1980 | 個案報告 | Sem Hosp Paris | 分泌 IgM 之原發性肺淋巴肉瘤以 Chlorambucil 持續治療，3 年追蹤顯示持續臨床緩解 |

---

## 細胞毒性

Chlorambucil 屬抗腫瘤烷化劑，具明確細胞毒性，適用本章節：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Nitrogen mustard 烷化劑） |
| 骨髓抑制風險 | 中至高度（嗜中性白血球減少、血小板減少、貧血常見；長期使用有劑量累積毒性） |
| 致吐性分級 | 低度（口服給藥，致吐風險相對低） |
| 監測項目 | CBC（含白血球分類）、肝腎功能；長期使用需追蹤繼發性血液惡性腫瘤（MDS/AML 風險） |
| 處置防護 | 需依細胞毒性藥物處置規範操作；具致畸胎性，育齡女性使用期間須採有效避孕措施 |

---

## 安全性考量

詳細警語、禁忌及藥物交互作用資料請參考原廠仿單（Leukeran®）或 EMA/FDA 核准說明書（DG001 尚待補充）。

依公開文獻已知之重要安全性考量：

- **繼發性惡性腫瘤**：長期使用與繼發性 AML、MDS 及實體腫瘤風險增加有關（PMID [1392790](https://pubmed.ncbi.nlm.nih.gov/1392790/)、[9000608](https://pubmed.ncbi.nlm.nih.gov/9000608/)）
- **生殖毒性**：具致畸胎性，孕婦禁用
- **神經毒性（高劑量）**：高劑量脈衝式給藥可引起抽搐，為劑量限制性毒性（PMID [3179770](https://pubmed.ncbi.nlm.nih.gov/3179770/)）

---

## 結論與下一步

**決策：Hold**

**理由：**
Chlorambucil 對廣義 CLL 的療效已有多項 Phase 3 試驗間接支持，TxGNN 對 IGHV 突變型 CLL/SLL 亞型的預測在機轉上合理；然而此特定分子亞型缺乏直接臨床試驗與文獻（L5 級），且當前標靶藥物（ibrutinib/venetoclax）療效已優於 Chlorambucil 並逐漸取代其在第一線的地位，加上香港未有上市許可，目前不具推進優先性。

**若要推進需要：**

- 提取已完成的廣義 CLL Phase 3 試驗中 IGHV 突變狀態分層的次族群分析數據（subgroup analysis）
- 取得完整 DrugBank 作用機轉資料（DG002）及香港/原廠仿單警語（DG001）
- 確認 Chlorambucil 在香港的合法取得途徑（如特殊進口申請）
- 諮詢血液腫瘤科專家評估：在 ibrutinib/venetoclax 時代，Chlorambucil 在 IGHV 突變型 CLL 中的現代定位是否仍有臨床價值（例如高齡共病族群）
- 評估是否優先考慮廣義 CLL（非特定分子亞型）的臨床應用路徑

---
*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

