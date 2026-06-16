---
layout: default
title: Dexamethasone
parent: 高證據等級 (L1-L2)
nav_order: 224
evidence_level: L2
indication_count: 10
---

# Dexamethasone
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Dexamethasone：從廣效抗炎免疫抑制到斑禿 (Alopecia Areata)

## 一句話總結

Dexamethasone 是一種強效糖皮質激素，廣泛用於炎症、自體免疫疾病及過敏反應的臨床治療。TxGNN 模型預測它可能對**斑禿 (Alopecia Areata)** 有效，目前有 **1 項 RCT**、**1 篇系統性回顧及網絡 Meta 分析**，以及共 **20 篇文獻**支持這個方向，機轉聯繫明確。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 炎症、自體免疫疾病、過敏反應（廣效糖皮質激素） |
| 預測新適應症 | 斑禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2 |
| 香港上市 | 資料庫無記錄（請向衞生署核實） |
| 許可證數 | 0 張（資料庫查詢結果） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

斑禿（Alopecia Areata, AA）是一種由 **CD8+ T 細胞介導的自體免疫疾病**。這些 T 細胞攻擊毛囊，破壞毛囊正常的「免疫豁免微環境」（immune privilege），導致非瘢痕性、可逆性落髮。由於其核心病理機轉為免疫失調，免疫抑制藥物在理論上具備介入空間。

Dexamethasone 作為強效糖皮質激素，透過以下多重機轉可能對 AA 產生療效：**抑制 NF-κB 訊號通路**以降低促炎細胞激素生成；**下調 IFN-γ、IL-15、IL-2** 等驅動 T 細胞活化的關鍵訊號；以及**減少 CD8+ T 細胞增殖與毛囊周圍浸潤**，從而恢復毛囊免疫豁免。

臨床上發展出的「**口服迷你脈衝療法（Oral Mini-Pulse, OMP）**」策略——通常為每週末連續 2 天口服 Dexamethasone 5 mg——在兼顧療效的同時，大幅降低長期連續使用系統性類固醇所帶來的副作用（如下丘腦-垂體-腎上腺軸抑制、骨質疏鬆）。此療法已有多年臨床使用經驗，並有直接的 RCT 與多項前瞻性研究支持。

---

## 臨床試驗證據

本次 ClinicalTrials.gov 查詢返回 14 個試驗，但經相關性評估，**所有試驗均為腫瘤科試驗（相關性等級 C）**，Dexamethasone 在其中作為止吐前驅用藥、過敏預防用藥或化療方案組成部分（如多發性骨髓瘤 VRD/DVD 方案），與斑禿適應症無直接關聯。

目前無直接以 Dexamethasone 作為主要介入措施治療斑禿的登記臨床試驗。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | **RCT** | Dermatologic Therapy | 隨機對照試驗：比較低劑量 Dexamethasone OMP 與 DPCP 接觸致敏療法治療嚴重兒童斑禿，評估有效性與安全性 |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | 系統性回顧 + 網絡 Meta 分析 | Archives of Dermatological Research | 比較系統性類固醇、口服 JAK 抑制劑及接觸免疫療法對嚴重斑禿（SALT ≥50%）之療效，為指引提供證據等級 |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | 前瞻性佇列研究 | Journal of Clinical Medicine | 真實世界證據：評估 Dexamethasone 迷你脈衝療法的有效性、安全性及治療反應相關預測因子 |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | 病例系列 + 文獻回顧 | J Dermatological Treatment | JAK 抑制劑不可及時，Dexamethasone OMP 可誘導嚴重斑禿持久緩解，提供替代方案文獻回顧 |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | 前瞻性佇列研究（多中心） | Dermatologic Therapy | 多中心研究：口服 Dexamethasone 迷你脈衝治療中重度斑禿（含全禿/普禿），評估反應率及復發情況 |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | 前瞻性研究 | Dermatologic Therapy | 比較 1 天 vs 3 天靜脈 Dexamethasone 脈衝聯合外用 Clobetasol 治療嚴重兒童斑禿（n=73） |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | 縱向佇列研究 | Dermatologic Therapy | 長期隨訪（中位 96 個月）：口服 Dexamethasone 脈衝聯合外用皮質類固醇治療 65 名嚴重兒童 AA |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | 文獻回顧 | Pediatric Dermatology | 系統整理兒童斑禿脈衝劑量皮質類固醇療法的各種劑量方案及相關副作用文獻 |
| [41872082](https://pubmed.ncbi.nlm.nih.gov/41872082/) | 2026 | 回顧性真實世界研究 | European Journal of Dermatology | 分步外用類固醇聯合 Baricitinib、以 Dexamethasone 脈衝作為救援策略，強化嚴重 AA 療效（n=19） |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | 比較性研究 | Dermatology (Basel) | 比較三種系統性皮質類固醇療法對廣泛性斑禿的療效、復發率與副作用，提供 Dexamethasone 相對定位 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：系統性 Dexamethasone 長期使用已知副作用包括下丘腦-垂體-腎上腺軸抑制、高血糖、高血壓、骨質疏鬆、白內障、眼壓升高及感染風險增加。「迷你脈衝療法」策略的設計正是為了緩解上述風險，但仍須定期監測。此外，**長期使用 Dexamethasone 本身亦為休止期落髮（Telogen Effluvium）的已知致因**，在 AA 治療中需關注此反向風險並與患者充分溝通。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有 1 項 RCT 及 1 篇系統性回顧 + 網絡 Meta 分析直接支持 Dexamethasone 用於斑禿的臨床療效，並有多項前瞻性佇列研究提供真實世界證據。口服迷你脈衝療法在機轉上合理（免疫豁免恢復）、在臨床上具有可操作性（尤其在 JAK 抑制劑不可及的情況下），且已有 20 年以上的使用經驗。主要限制在於尚無大型 Phase 3 RCT，且長期系統性類固醇副作用需嚴格管控。

**若要推進需要：**
- 補充 Dexamethasone 完整作用機轉資料（DrugBank MOA）及藥物分類
- 向香港衞生署藥劑業及毒藥管理局確認現行許可證狀態及已批准適應症，並取得完整仿單
- 制定標準化迷你脈衝療法給藥方案，並設立安全性監測計畫（空腹血糖、血壓、骨密度、眼壓、HPA 軸功能）
- 界定適合族群（特別是 JAK 抑制劑禁忌或不可及患者）及排除標準（糖尿病、活動性感染、骨質疏鬆等）
- 評估與 JAK 抑制劑（如 Baricitinib）的序列或聯合治療策略，參考最新 2026 年真實世界資料（PMID 41872082）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

