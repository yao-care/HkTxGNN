---
layout: default
title: Gimeracil
parent: 高證據等級 (L1-L2)
nav_order: 347
evidence_level: L1
indication_count: 5
---

# Gimeracil
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

# Gimeracil：從 S-1 複方 DPD 抑制劑到大腸腫瘤

## 一句話總結

Gimeracil 是 S-1 複方（tegafur + gimeracil + oteracil）的核心成分之一，透過抑制 DPD（二氫嘧啶去氫酶）延長 5-FU 體內半衰期，發揮藥動學增效作用。
TxGNN 模型預測它可能對**大腸腫瘤 (Colonic Neoplasm)** 有效，
目前有 **8 個臨床試驗**支持這個方向（其中 2 個已完成 Phase 3 RCT）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | S-1 複方成分（消化道腫瘤藥動學增效） |
| 預測新適應症 | 大腸腫瘤 (Colonic Neoplasm) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Gimeracil 是 S-1 複方的關鍵功能成分，其作用是選擇性抑制 DPD（dihydropyrimidine dehydrogenase），阻斷氟尿嘧啶（5-FU）在腸道黏膜的快速代謝，使活性成分在腫瘤部位維持較高濃度，從而提升整體抗腫瘤效果。

消化道腫瘤（胃癌、大腸癌）在組織病理和藥理機轉上高度相似，均屬氟尿嘧啶類敏感腫瘤。S-1 複方早已在日本、韓國及台灣取得大腸直腸癌適應症，臨床上被廣泛使用，因此 TxGNN 對含 Gimeracil 的複方成分預測至大腸腫瘤，具有充分的生物學合理性。

最重要的是，目前已有 **兩項 Phase 3 RCT 完成**：一項針對 Stage III 結腸癌輔助化療（1535 人），另一項針對轉移性結直腸癌一線治療（161 人），均直接評估含 Gimeracil 的 S-1 複方，且達到主要終點，提供 L1 等級的最強臨床證據。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | 已完成 | 1535 | S-1 vs UFT+Leucovorin 用於 Stage III 結腸癌輔助化療，探討基因表現預測因子；為最大規模直接證據 |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | 已完成 | 161 | SALTO 研究：S-1 vs Capecitabine 一線治療轉移性結直腸癌，評估口服氟尿嘧啶類的安全性差異 |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | 不明 | 1191 | SOX（S-1 + Oxaliplatin）vs XELOX 用於 Stage III 結直腸癌輔助化療，主要終點為 5 年 DFS |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | 不明 | 82 | Raltitrexed + S-1 聯合方案評估標準化療失敗後轉移性結直腸癌，主要終點為 mPFS |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | 尚未招募 | 52 | Fuquinitinib + Tegafur/Gimeracil/Oteracil 三線治療晚期轉移性結直腸癌；代表複方在當代聯合療法持續被研究 |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | 不明 | 42 | SOL 方案（S-1 + 口服 Leucovorin + Oxaliplatin）用於未治療轉移性結直腸癌，探索劑量安全性與初步療效 |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | 不明 | 40 | S-1 + Bevacizumab 聯合方案用於先前 Irinotecan 及 Oxaliplatin 治療失敗的復發性結直腸癌 |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | 提前終止 | 20 | 評估 S-1+Oxaliplatin vs Capecitabine+Oxaliplatin 對冠狀動脈血流影響；因心血管安全顧慮提前終止，揭示 Guardrails 需求 |

---

## 香港上市資訊

Gimeracil（DrugBank DB09257）目前在香港未有獨立上市許可，亦無任何相關藥品許可登記。

> 注意：Gimeracil 通常以複方形式存在（S-1），而非單獨製劑上市。若評估 S-1 複方整體的香港許可狀態，需另行查詢 tegafur/gimeracil/oteracil 組合製劑的登記資料。

---

## 細胞毒性

Gimeracil 為 S-1 複方（氟尿嘧啶類抗腫瘤藥物）的組成成分，屬抗腫瘤藥物範疇，適用本章節。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | DPD 抑制劑（藥動學增效成分）／氟尿嘧啶類複方成分 |
| 骨髓抑制風險 | 中度（透過增強 5-FU 系統曝露，間接升高嗜中性白血球減少及血小板減少風險） |
| 致吐性分級 | 低至中度（S-1 口服製劑致吐性低於靜脈 5-FU） |
| 監測項目 | CBC（含白血球分類）、肝腎功能（AST/ALT/Cr）、口腔黏膜評估 |
| 處置防護 | 需依細胞毒性藥物處置規範操作；備孕或懷孕者禁用 |

> 詳細毒性資料請參考原廠 S-1 仿單的警語與注意事項。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
已有兩項完成的 Phase 3 RCT（NCT00660894，1535 人；NCT01918852，161 人）直接評估含 Gimeracil 的 S-1 複方用於結腸癌，達 L1 證據等級，支持推進評估；
然而 Gimeracil 在香港未有獨立上市許可、安全性資料（仿單警語與禁忌）尚待確認，且一項試驗（NCT02216149）因心血管安全顧慮提前終止，需納入監測計畫。

**若要推進需要：**
- 取得 S-1 複方仿單（TFDA 或日本 PMDA 版本），確認警語、禁忌與藥物交互作用
- 向香港衛生署查詢 S-1 複方（tegafur/gimeracil/oteracil）的本地許可現況或特別用藥申請途徑
- 補充 Gimeracil 的 DrugBank MOA 詳細資料，以強化機轉關聯性分析
- 針對心血管安全性（尤其冠狀動脈相關風險），制定治療前風險評估及療程中監測計畫
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

