---
layout: default
title: Topotecan
parent: 高證據等級 (L1-L2)
nav_order: 759
evidence_level: L2
indication_count: 5
---

# Topotecan
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

# Topotecan：從（原適應症資料缺失）到乳癌

## 一句話總結

Topotecan 是一種 Topoisomerase I 抑制劑類化療藥物，但本次 Evidence Pack 未提供其在香港核准的原始適應症與作用機轉資料。
TxGNN 模型預測它可能對**乳癌 (Female Breast Carcinoma)** 有效，
目前有 **5 個相關臨床試驗**和 **20+ 篇文獻**支持這個方向，但多數為早期或已終止的研究。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（無許可證/適應症紀錄） |
| 預測新適應症 | 乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold（原始評分建議：Research Question） |

---

## 為什麼這個預測合理？

目前缺乏 Topotecan 詳細的作用機轉資料（MOA data gap），本節說明改依 Evidence Pack 中的機轉關聯性分析（repurposing_rationale）進行推論。

Topotecan 為 Topoisomerase I 抑制劑（camptothecin 衍生物），文獻證據顯示乳癌細胞、尤其是 MYC 驅動或三陰性乳癌（TNBC）亞型，對 R-loop 累積及複製壓力具有較高敏感性，理論上存在合成致死（synthetic lethality）潛力（PMID 37987734、40300683 為機轉層級的臨床前證據）。

然而，乳癌並非 Topotecan 目前公認的核准適應症。自 1990 年代起已有多個 Phase II 單藥或合併療法試驗（如 CALGB 研究 PMID 10362325、TIME regimen NCT00006032）評估其在轉移性乳癌的活性，但整體反應率僅約 10-20%，屬中等偏低，且未轉化為指引建議或核准適應症。近期進行中的複方試驗（如 NCT04739800）主要針對卵巢癌族群，非直接以乳癌為主要適應症。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | 已終止 | N/A | TIME regimen（Topotecan+Ifosfamide+Etoposide）併自體幹細胞救援治療轉移性乳癌，以 Topotecan 為核心藥物，惟試驗已終止 |
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | 進行中（未招募） | 120 | Durvalumab+Olaparib+Cediranib 三藥合併療法，用於鉑抗藥性復發卵巢癌／原發腹膜癌／輸卵管癌族群 |
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | 已完成 | 266 | Olaparib 單藥 vs. 醫師選擇之單藥化療，用於 BRCA1/2 突變鉑敏感復發卵巢癌，關聯性存疑（標題截斷無法確認 Topotecan 角色） |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | 已終止 | 221 | Selinexor 併多種標準化療/免疫療法（含 Topotecan）於晚期惡性腫瘤之安全性試驗 |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | 未知 | 35 | 以病人衍生類器官（organoid）高通量藥物篩選平台選擇難治實體瘤化療方案，屬驗證性平台研究 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | Phase II Cohort (CALGB) | Am J Clin Oncol | CALGB 主導之晚期乳癌 Phase II 試驗，53 名先前接受過化療病人中 40 人可評估療效 |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Phase II Pilot | Onkologie | Topotecan 用於乳癌腦轉移病人之先導性化療研究 |
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Phase II | Br J Cancer | 持續輸注 Topotecan 於晚期乳癌與 NSCLC，未顯示療效優於間歇給藥 |
| [9626200](https://pubmed.ncbi.nlm.nih.gov/9626200/) | 1998 | Phase II | J Clin Oncol | Paclitaxel+Topotecan 併 G-CSF 支持治療第四期乳癌之多中心試驗 |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | Preclinical | Int J Biol Macromol | TFDP1 為 TNBC 治療標的，與 Topotecan 療效機轉相關 |
| [37987734](https://pubmed.ncbi.nlm.nih.gov/37987734/) | 2023 | Preclinical/Mechanistic | Cancer Research | MYC 驅動乳癌中 Topo I 抑制誘發 R-loop 累積之合成致死機轉 |
| [26623560](https://pubmed.ncbi.nlm.nih.gov/26623560/) | 2015 | Preclinical | Oncotarget | Metronomic Topotecan+Pazopanib 併用於三陰性乳癌臨床前模型 |
| [31408695](https://pubmed.ncbi.nlm.nih.gov/31408695/) | 2019 | Preclinical | Pharmacol Res | Daidzein 增強 Topotecan 抗癌效果並逆轉乳癌 BCRP 抗藥性 |
| [15836850](https://pubmed.ncbi.nlm.nih.gov/15836850/) | 2005 | Preclinical | J Surg Res | Quercetin 對 MCF-7 與 MDA-MB-231 乳癌細胞中 Topotecan 細胞毒性之影響 |
| [10930538](https://pubmed.ncbi.nlm.nih.gov/10930538/) | 2000 | Preclinical | Biochem Pharmacol | Topotecan 抗藥性人類乳癌細胞株之 BCRP/MXR/ABCP 表現研究 |

---

## 香港上市資訊

目前 Topotecan 未在香港上市，無許可證資料可供列出。

---

## 細胞毒性

Topotecan 為 Camptothecin 衍生之 Topoisomerase I 抑制劑，屬傳統細胞毒性化療藥物（文獻中明確描述其為 "chemotherapeutic agent" / "cytotoxic effect"，見 PMID 31408695、15836850）。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Camptothecin 衍生物、Topoisomerase I 抑制劑） |
| 骨髓抑制風險 | 高 — 文獻顯示為主要劑量限制毒性（PMID 8617580：中位最低點白血球 1.75×10³/mm³、嗜中性球 1.55×10³/mm³、血小板 20,500/mm³） |
| 致吐性分級 | 中度 |
| 監測項目 | CBC（含白血球分類計數）、肝腎功能、電解質 |
| 處置防護 | 需依細胞毒性藥物處置規範操作（配製、給藥、廢棄物處理） |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**（Evidence Pack 原始評分建議為 "Research Question"）

**理由：**
- 雖整體證據等級達 L2，但真正直接針對「乳癌」適應症的臨床試驗多為 1990-2000 年代已完成之早期 Phase II 研究，反應率偏低（約 10-20%），未見近期確證性 Phase 3 試驗；唯一以 Topotecan 為核心之乳癌高劑量化療試驗（NCT00006032, TIME regimen）已終止。
- 機轉層級證據（MYC-driven synthetic lethality、TNBC 標靶潛力）具吸引力，但仍停留在臨床前階段，尚未轉譯為臨床試驗設計。
- 藥物目前未在香港上市，且缺乏 MOA 與仿單安全性資料（DG001 為 Blocking 等級缺口），無法進入 S1 安全性初評。

**若要推進需要：**
- 補齊 DrugBank MOA 資料（DG002）與香港衛生署仿單警語/禁忌（DG001，Blocking，需優先解決）
- 針對 TNBC/MYC 驅動亞型設計轉譯性或早期概念驗證（proof-of-concept）臨床試驗，銜接臨床前機轉證據
- 評估香港藥物上市可行性與相關法規路徑
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

