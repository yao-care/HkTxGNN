---
layout: default
title: Bempedoic Acid
parent: 中證據等級 (L3-L4)
nav_order: 87
evidence_level: L3
indication_count: 10
---

# Bempedoic Acid
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Bempedoic Acid：從高膽固醇血症到純合子家族性高膽固醇血症

## 一句話總結

Bempedoic acid 是一種口服 ATP-citrate lyase (ACL) 抑制劑，透過抑制肝細胞膽固醇合成途徑來降低 LDL-C，用於高膽固醇血症的治療。TxGNN 模型所有預測中，對**純合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia, HoFH)** 的預測具最強實際臨床支持，目前有 **0 個臨床試驗**和 **17 篇文獻**支持此方向，其中包含 1 篇 2026 年真實世界研究。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | LDL-C 降低療法（高膽固醇血症；香港許可證資料未載入） |
| 預測新適應症 | 純合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia) |
| TxGNN 預測分數 | 99.48%（全模型排名第 9,188） |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏原廠詳細作用機轉資料（Data Gap）。根據已知文獻，Bempedoic acid 是一種口服小分子 ACL 抑制劑，透過抑制肝細胞中的 **ATP-citrate lyase**，減少胞漿內 acetyl-CoA 的供應，從而壓制 HMG-CoA reductase 上游合成底物，降低肝臟膽固醇合成量，並代償性上調肝細胞表面 LDL 受體表現，促進血液中 LDL-C 的清除。此藥的作用位點限於肝細胞，因此骨骼肌相關不良反應（如 statin 肌病變）風險理論上較低。

**純合子家族性高膽固醇血症 (HoFH)** 由 LDLR（最常見）、APOB 或 PCSK9 基因的雙等位基因突變所致，LDL 受體功能嚴重缺失（殘餘活性通常 < 2%），血清 LDL-C 極度升高（常超過 400 mg/dL），患者幼年期即出現早發性動脈粥樣硬化心血管疾病（ASCVD）。HoFH 全球盛行率約 1/300,000，屬罕見病。

Bempedoic acid 對 HoFH 的預測合理性在於：儘管 LDL 受體功能嚴重缺乏使其**單藥療效有限**，但在多藥聯合策略中（搭配 evinacumab、lomitapide、PCSK9 抑制劑或 LDL 分離置換術）可提供額外約 **15–25% 的 LDL-C 降幅**，作為輔助用藥具有實際臨床價值。2026 年發表的真實世界研究（PMID 41274797）已初步評估此輔助角色的療效與耐受性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | 真實世界／回顧性研究 | J Clin Lipidology | 評估 bempedoic acid 在 HoFH 患者中的療效與耐受性，初步驗證輔助降脂角色 |
| [29449335](https://pubmed.ncbi.nlm.nih.gov/29449335/) | 2018 | 動物試驗（前臨床） | Arterioscler Thromb Vasc Biol | Bempedoic acid 在 LDLR 缺乏型 Yucatan 迷你豬中降低 LDL-C 並顯著減緩動脈粥樣硬化進程 |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | 文獻回顧 | Exp Mol Pathol | HoFH 創新療法全面綜述，涵蓋 bempedoic acid 在多藥聯合策略中的定位 |
| [41741298](https://pubmed.ncbi.nlm.nih.gov/41741298/) | 2026 | 臨床共識 | J Clin Lipidology | NLA 家族性高膽固醇血症臨床共識更新，含 HoFH 診斷與治療指引 |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | 文獻回顧 | J Atherosclerosis Thrombosis | HoFH 治療進展綜述，強調多藥積極聯合降脂策略的必要性 |
| [37071085](https://pubmed.ncbi.nlm.nih.gov/37071085/) | 2024 | 藥物回顧 | Cardiology in Review | Evinacumab 用於 HoFH 治療綜述，討論 bempedoic acid 作為補充療法 |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | 專題回顧 | JACC | 新興 LDL-C 降低療法綜述，涵蓋 bempedoic acid、inclisiran 等在家族性高膽固醇血症的角色 |
| [34081216](https://pubmed.ncbi.nlm.nih.gov/34081216/) | 2021 | 文獻回顧 | Curr Cardiol Reports | 家族性與難治性高膽固醇血症的 statin/PCSK9i 以外治療選項更新 |
| [38576462](https://pubmed.ncbi.nlm.nih.gov/38576462/) | 2024 | 文獻回顧 | Am J Prev Cardiol | LDL-C 長期積極降低對 ASCVD 預防的臨床意義，支持 HoFH 早期強化治療 |
| [39070027](https://pubmed.ncbi.nlm.nih.gov/39070027/) | 2024 | 文獻回顧 | Am J Prev Cardiol | PCSK9 抑制劑及更多 LDL-C 靶向療法進展，含 bempedoic acid 的聯合應用 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
2026 年真實世界研究已初步驗證 bempedoic acid 在 HoFH 患者中的可行性，多篇高品質文獻回顧及 NLA 臨床共識亦支持其作為多藥聯合策略輔助降脂的臨床合理性；然而目前缺乏前瞻性 RCT 數據，藥物在香港未上市，且原廠安全性資料（警語、禁忌症）尚未取得，需在監控條件下審慎推進。

**若要推進需要：**
- 補充詳細 MOA 原廠資料（查詢 DrugBank API，填補 Data Gap DG002）
- 下載並解析原廠仿單 PDF，取得完整警語與禁忌症（填補 Data Gap DG001）
- 設計以 HoFH 為目標族群的前瞻性臨床試驗，評估 bempedoic acid 於多藥聯合策略中的 LDL-C 降幅及安全性
- 評估與 evinacumab、lomitapide 聯合使用的藥物交互作用風險
- 調查港台地區 HoFH 患者人數，評估孤兒藥資格（Orphan Drug Designation）申請可行性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

