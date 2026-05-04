---
layout: default
title: Bleomycin
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 6
---

# Bleomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Bleomycin：從惡性淋巴瘤到六項腫瘤適應症再利用分析

## 一句話總結

Bleomycin 為糖肽類抗腫瘤抗生素，文獻充分記載其作為 ABVD（Hodgkin's 淋巴瘤）及 BEP（生殖細胞瘤）方案核心藥物的臨床地位，但目前在香港尚未取得正式上市許可（0 張許可證）。TxGNN 模型共預測六項新適應症，最高評分為**馬尾神經腫瘤 (Cauda Equina Neoplasm)**（99.30%），最具臨床開發潛力者為**網狀細胞肉瘤 (Reticulum Cell Sarcoma)**——此為高度惡性 NHL 的舊稱，目前有 **3 個 Phase 3 RCT** 及 **20 篇以上文獻**（含 2 篇 RCT 及 1 篇匯總 RCT 分析）支持，整體證據等級達 **L1**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 已知原適應症 | 惡性淋巴瘤 / 生殖細胞瘤（依文獻推斷；香港無上市登記） |
| TxGNN 最高分預測 | 馬尾神經腫瘤 (Cauda Equina Neoplasm) |
| 最高預測分數 | 99.30% |
| 最佳證據適應症 | 網狀細胞肉瘤 (Reticulum Cell Sarcoma) |
| 最佳證據等級 | **L1**（具 Phase 3 RCT） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 整體建議決策 | **Proceed with Guardrails**（網狀細胞肉瘤）；Hold（其餘五項） |

---

## 六項預測適應症總覽

| 排名 | 適應症 | TxGNN 分數 | 臨床試驗數 | 文獻數 | 證據等級 | 建議 |
|------|--------|------------|-----------|--------|---------|------|
| 1 | 馬尾神經腫瘤 (Cauda Equina Neoplasm) | 99.30% | 0 | 3 | L4 | Hold |
| 2 | 成人星狀細胞瘤 (Adult Astrocytic Tumour) | 99.28% | 0 | 20 | L3 | Research Question |
| **3** | **網狀細胞肉瘤 (Reticulum Cell Sarcoma)** | **99.14%** | **13** | **20** | **L1** | **Proceed with Guardrails** |
| 4 | 原發性肺淋巴瘤 (Primary Pulmonary Lymphoma) | 99.10% | 8 | 20 | L2 | Research Question |
| 5 | 肺母細胞瘤 (Pulmonary Blastoma) | 99.04% | 0 | 2 | L4 | Hold |
| 6 | 高分化胎兒型肺腺癌 (Well-differentiated Fetal Adenocarcinoma of the Lung) | 99.03% | 0 | 0 | L5 | Hold |

---

## 為什麼這些預測合理？

目前缺乏詳細的作用機轉資料（DG002 資料缺口）。根據現有文獻推斷，Bleomycin 為糖肽類抗腫瘤抗生素，其作用機制為在鐵離子催化下產生羥基自由基，對 DNA 造成單鏈及雙鏈斷裂，屬細胞週期特異性（G₂/M 期）藥物。由於骨髓毒性低，Bleomycin 常被納入多藥聯合方案。此外，Bleomycin hydrolase（負責代謝失活）在肺組織及皮膚中活性偏低，正是肺毒性與皮膚毒性的主因。

**網狀細胞肉瘤（最高優先開發適應症）**：「網狀細胞肉瘤」為 Diffuse Large B-Cell Lymphoma（DLBCL）/ 高度惡性 NHL 的舊有分類術語。Bleomycin 作為 ProMACE-CytaBOM、CHVmP/BV、PMitCEBO 等多個 NHL 方案的核心成分，透過 DNA 鏈斷裂對快速增殖的 B 淋巴瘤細胞發揮細胞毒性，機轉合理性充分，且有 Phase 3 RCT 直接驗證。

**馬尾神經腫瘤（TxGNN 最高分，但 Hold）**：馬尾腫瘤涵蓋多種組織類型（脊膜瘤、神經纖維瘤、室管膜瘤、淋巴瘤、轉移性生殖細胞瘤）。若腫瘤屬淋巴瘤或 GCT 亞型，理論上有機轉連結；然而現有 3 篇文獻均為 CNS 淋巴瘤或 CNS GCT 的間接引用，未聚焦於馬尾神經定位。TxGNN 高分很可能源於圖譜中「脊椎腫瘤 → 淋巴瘤 → Bleomycin」的遠距離路徑傳播，而非直接生物學關聯。

**成人星狀細胞瘤（探索性，L3）**：Bleomycin 誘導的 DNA 雙鏈斷裂對增殖活躍的高度惡性膠質瘤細胞具理論細胞毒性，血腦屏障為主要藥動學障礙，但瘤內持續輸注（convection-enhanced delivery）可有效繞過此限制。1970–2000 年代有多篇臨床探索性文獻，包含一項 Phase I 瘤內持續輸注試驗（PMID 12416544）確認可行性。

**肺部相關適應症（原發性肺淋巴瘤、肺母細胞瘤、高分化胎兒型肺腺癌）**：需特別注意 Bleomycin 的主要毒性為肺纖維化，在肺部已受腫瘤侵犯的患者中使用，肺毒性風險疊加，效益風險比需特別謹慎評估。

---

## 【最高優先適應症】網狀細胞肉瘤 — 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00005867](https://clinicaltrials.gov/study/NCT00005867) | Phase 3 | 完成 | 310 | CHOP vs. PMitCEBO（含 bleomycin）隨機比較，良好預後侵襲性 NHL |
| [NCT00002835](https://clinicaltrials.gov/study/NCT00002835) | Phase 3 | 完成 | 116 | 早期強化 vs. 交替三聯療法（含 bleomycin 方案），中度 / 免疫母細胞型淋巴瘤 |
| [NCT00002565](https://clinicaltrials.gov/study/NCT00002565) | Phase 3 | 完成 | 61 | ATT vs. CHOP 於中度及免疫母細胞型 NHL |
| [NCT00002571](https://clinicaltrials.gov/study/NCT00002571) | Phase 2 | 完成 | 52 | ProMACE-CytaBOM + TMP-SMX/AZT/G-CSF 於 AIDS 相關淋巴瘤 |
| [NCT00003110](https://clinicaltrials.gov/study/NCT00003110) | Phase 2 | 完成 | 5 | 72 小時持續輸注 bleomycin 作為 AIDS 相關及免疫缺乏 NHL 救援療法（bleomycin 單藥試驗） |
| [NCT00057811](https://clinicaltrials.gov/study/NCT00057811) | Phase 2 | 完成 | 97 | Rituximab 加入含 bleomycin 誘導鞏固方案，兒童新診斷進展期 B 細胞淋巴瘤 |
| [NCT00002524](https://clinicaltrials.gov/study/NCT00002524) | Phase 2 | 完成 | 46 | AIDS 相關淋巴瘤先導研究，多藥聯合含 bleomycin 方案 |
| [NCT00032149](https://clinicaltrials.gov/study/NCT00032149) | Phase 1/2 | 未知 | 30 | PMitCEBO + G-CSF 於良好預後 HIV 相關淋巴瘤 |
| [NCT00002657](https://clinicaltrials.gov/study/NCT00002657) | Phase 2 | 完成 | 20 | ProMACE-CytaBOM 序貫免疫抑制調整，心臟移植後淋巴增殖症 |
| [NCT00031902](https://clinicaltrials.gov/study/NCT00031902) | Phase 1 | 未知 | N/A | Rituximab + PVB（含 bleomycin）於不良預後 HIV 相關 NHL |

---

## 【最高優先適應症】網狀細胞肉瘤 — 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1699653](https://pubmed.ncbi.nlm.nih.gov/1699653/) | 1990 | RCT | Cancer | 隨機比較 CHOP ± bleomycin ± 高劑量 MTX 於 DLCL 等 NHL（n=274），Cancer and Leukemia Group B |
| [14962711](https://pubmed.ncbi.nlm.nih.gov/14962711/) | 2004 | Pooled RCT Analysis | Eur J Cancer | 三個 EORTC 試驗匯總（n=936），CHVmP/BV（含 bleomycin）vs. 無 bleomycin 方案長期療效比較 |
| [7680764](https://pubmed.ncbi.nlm.nih.gov/7680764/) | 1993 | RCT | NEJM | SWOG 試驗（n=899），CHOP vs. 含 bleomycin 之第二/三代方案，確立 CHOP 標準地位 |
| [4109401](https://pubmed.ncbi.nlm.nih.gov/4109401/) | 1972 | Early Clinical Trial | BMJ | Bleomycin 單藥於網狀細胞肉瘤（n=22）及 Hodgkin's（n=54），29% Hodgkin's 完全緩解 |
| [65728](https://pubmed.ncbi.nlm.nih.gov/65728/) | 1977 | Early RCT | Med Pediatr Oncol | CVP vs. ABP（含 bleomycin）隨機比較，IV 期 NHL（n=57） |
| [10192438](https://pubmed.ncbi.nlm.nih.gov/10192438/) | 1999 | Prospective Cohort | Br J Haematol | VACOP-B（含 bleomycin）後高劑量 CBV + 自體幹細胞移植，大細胞 NHL 風險適應治療 |
| [37294956](https://pubmed.ncbi.nlm.nih.gov/37294956/) | 2023 | Review | Hematol Oncol | 妊娠期淋巴瘤：HL 孕期 ABVD 安全性、侵襲性 NHL 治療選擇 |
| [6205233](https://pubmed.ncbi.nlm.nih.gov/6205233/) | 1984 | Review | Med Clin North Am | 非霍奇金淋巴瘤化療與放療綜述，bleomycin 方案療效分析 |
| [7535348](https://pubmed.ncbi.nlm.nih.gov/7535348/) | 1994 | Case Series | J Chemotherapy | 胸腔內注射 bleomycin 治療 NHL 引致乳糜胸，3 例均達完全緩解 |
| [15934513](https://pubmed.ncbi.nlm.nih.gov/15934513/) | 2005 | Review | Oncology | GELA 多項 Phase 2/3 研究回顧，DLBCL 及 T 細胞淋巴瘤治療演進 |

---

## 【次優先適應症】原發性肺淋巴瘤 — 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03159897](https://clinicaltrials.gov/study/NCT03159897) | Phase 3 | 完成 | 500 | 劑量密集/劑量強化 ABVD vs. PET 導向 ABVD（含 bleomycin），進展期 HL（FIL-Rouge 試驗） |
| [NCT05675410](https://clinicaltrials.gov/study/NCT05675410) | Phase 3 | 招募中 | 1,875 | 標準 ABVD（含 bleomycin）vs. 免疫腫瘤學方案，I-II 期經典型 HL，當前最大規模相關試驗 |
| [NCT00165438](https://clinicaltrials.gov/study/NCT00165438) | N/A | 完成 | 60 | 前瞻性肺功能縱貫研究：bleomycin 化療 ± 縱隔放療對 HL 患者肺功能影響（直接肺毒性數據） |
| [NCT00352027](https://clinicaltrials.gov/study/NCT00352027) | Phase 2 | 完成 | 81 | Stanford V（含 bleomycin）聯合低劑量放療，兒科中危 HL |
| [NCT02247869](https://clinicaltrials.gov/study/NCT02247869) | Phase 2 | 完成 | 100 | 劑量密集 ABVD 於早期不良預後 HL |

> ⚠️ **特別提示**：原發性肺淋巴瘤（PPL）患者肺部已受腫瘤侵犯，使用 Bleomycin 可能疊加肺纖維化風險，效益風險比需個案審慎評估。以上試驗均針對普通 HL，非 PPL 特定試驗。

---

## 【探索性適應症】成人星狀細胞瘤 — 重點文獻

| PMID | 年份 | 類型 | 主要發現 |
|------|-----|------|---------|
| [12416544](https://pubmed.ncbi.nlm.nih.gov/12416544/) | 2002 | Phase I Trial | 瘤內持續輸注 bleomycin（可補充裝置）治療復發性 GBM，Phase I 可行性確認 |
| [6164465](https://pubmed.ncbi.nlm.nih.gov/6164465/) | 1981 | RCT | 斯堪地納維亞多中心 RCT（n=118），術後放療 ± bleomycin 靜脈輸注，未見 bleomycin 協同增效 |
| [1698540](https://pubmed.ncbi.nlm.nih.gov/1698540/) | 1990 | Phase II | 鈣調蛋白抑制劑 + bleomycin Phase II 試驗，GBM，有早期臨床活性訊號 |
| [77898](https://pubmed.ncbi.nlm.nih.gov/77898/) | 1978 | Non-RCT | 放療 + CCNU/procarbazine/bleomycin 聯合方案，高度 astrocytoma（n=20） |
| [55988](https://pubmed.ncbi.nlm.nih.gov/55988/) | 1975 | In vitro | BLM 對 8 例 astrocytoma 細胞株增殖抑制效果評估 |

---

## 香港上市資訊

Bleomycin 目前在香港**尚未取得藥劑製品登記（未上市）**，無相關許可證記錄。如需在香港應用，需通過醫院藥事委員會個案申請或藥物進口特別許可機制。

---

## 細胞毒性

Bleomycin 為確認之抗腫瘤抗生素，屬抗腫瘤藥物，此章節適用。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（糖肽類抗腫瘤抗生素） |
| 骨髓抑制風險 | **低**（Bleomycin 骨髓毒性低為其特點，常作為骨髓保留性藥物加入聯合方案） |
| 致吐性分級 | 低（單藥；聯合方案視其他成分而定） |
| 主要器官毒性 | **肺毒性**為最重要限制性毒性（bleomycin-induced pneumonitis → 肺纖維化）；皮膚毒性（色素沉著、皮膚硬化）；急性高熱 / 類過敏反應（偶可致命） |
| 監測項目 | 肺功能（DLCO、FVC，基線及每 2 週期後）、胸部 X 光 / CT（定期）、體溫（每次給藥前後）、腎功能（影響清除率）、**累積劑量記錄**（安全閾值 ≤ 400 units） |
| 處置防護 | 需依細胞毒性藥物處置規範操作；**首次給藥需先給測試劑量**（1–2 units），觀察 1–4 小時確認無急性反應後方可繼續 |

---

## 安全性考量

**主要警語**（依文獻推斷）：
- **肺毒性**：Bleomycin-induced pneumonitis (BPT) 及肺纖維化，高風險因素包括：累積劑量 > 400 units、年齡 > 70 歲、腎功能不全、同步/既往縱隔放療、術中高吸入氧濃度（應通知麻醉科）
- **急性高熱/類過敏反應**：即使既往耐受者仍可能發生致命性高熱反應（PMID [6187214](https://pubmed.ncbi.nlm.nih.gov/6187214/)）；每次給藥前需評估，首次使用須給測試劑量
- **放療疊加風險**：BPT 可能增加後續放射性肺炎風險（PMID [27742539](https://pubmed.ncbi.nlm.nih.gov/27742539/)），縱隔淋巴瘤患者尤需注意

> 詳細安全性資訊（仿單警語、禁忌）目前存在資料缺口（DG001：Blocking），待取得原廠仿單後補充完整評估。

---

## 結論與下一步

**決策：Proceed with Guardrails（限網狀細胞肉瘤 / 高度惡性 NHL 適應症）**

**理由：**
網狀細胞肉瘤（DLBCL / 高度惡性 NHL 之舊稱）擁有多個 Phase 3 RCT 直接支持含 bleomycin 方案的療效（包含 n=310 的 CHOP vs. PMitCEBO 比較試驗），加上 20 篇以上文獻（含 2 篇 RCT 及 1 篇三試驗匯總分析），證據等級達 L1，機轉亦明確可信；而 Bleomycin 低骨髓抑制的特性使其在聯合化療中具獨特地位。香港雖無登記上市，但全球主要地區均有大量使用經驗，可支持以特別申請方式引入。

**若要推進需要：**
- 取得 Bleomycin 在香港的藥物進口特別許可，評估供應鏈可行性
- 補充原廠仿單警語與禁忌資訊（DG001，Blocking 缺口，需優先解決）
- 透過 DrugBank API 補充正式 MOA 資料（DG002，High 缺口）
- 制定肺功能縱貫監測計畫（DLCO 基線 + 每 2 週期追蹤）及累積劑量管理協議（≤ 400 units）
- 訂定首次給藥測試劑量流程及急性高熱應對預案
- 針對原發性肺淋巴瘤及星狀細胞瘤適應症，建議先完成系統性文獻回顧（Research Question 決策階段），再決定是否啟動探索性研究
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

