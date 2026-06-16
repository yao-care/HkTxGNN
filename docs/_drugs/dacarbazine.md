---
layout: default
title: Dacarbazine
parent: 中證據等級 (L3-L4)
nav_order: 204
evidence_level: L4
indication_count: 1
---

# Dacarbazine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# DACARBAZINE：從黑色素瘤到上呼吸消化道腫瘤

## 一句話總結

DACARBAZINE 是一種烷化劑，國際上核准用於黑色素瘤及霍奇金淋巴瘤的治療，但目前在台灣尚未取得上市許可。
TxGNN 模型預測它可能對**上呼吸消化道腫瘤 (Upper Aerodigestive Tract Neoplasm)** 有效，
目前有 **1 個臨床試驗**（採用共享活性代謝物之 Temozolomide）和 **20 篇文獻**提供相關資訊。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 黑色素瘤、霍奇金淋巴瘤（國際核准；台灣未取得許可證） |
| 預測新適應症 | 上呼吸消化道腫瘤 (Upper Aerodigestive Tract Neoplasm) |
| TxGNN 預測分數 | 99.26% |
| 證據等級 | L4 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA Data Gap）。根據已知資訊，DACARBAZINE 是一種咪唑四氮雜類烷化劑，須經肝臟代謝後產生活性代謝物 MTIC（甲基三氮烯咪唑醯胺）。MTIC 透過甲基化 DNA O⁶ 位鳥嘌呤，誘導錯配修復（MMR）途徑失效，最終導致 DNA 雙鏈斷裂與細胞凋亡。值得注意的是，Temozolomide（另一種可直接產生 MTIC 的口服烷化劑）與 DACARBAZINE 共享此活性代謝物，兩者在機轉上具有高度相關性。

上呼吸消化道腫瘤（UADT）涵蓋口腔、咽喉、喉部、鼻腔、鼻竇及食道等部位的惡性腫瘤。這類腫瘤細胞增殖旺盛，部分具有 MGMT 啟動子甲基化特徵，理論上對烷化劑誘發的 DNA 損傷應具敏感性，此為 TxGNN 預測的機轉基礎。

然而，現有證據提供了重要的警示訊號：唯一相關的臨床試驗（NCT00423150，使用共享 MTIC 之 Temozolomide）在 86 人入組後即遭提前終止，顯示此烷化機轉在 UADT 的臨床轉化並不順利。可能原因包括：UADT 腫瘤中 MGMT 非甲基化比例過高、腫瘤微環境抵抗，或單藥療效本身不足。因此，雖然機轉假設具有一定合理性，直接的臨床可行性仍存在重大疑問。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00423150](https://clinicaltrials.gov/study/NCT00423150) | Phase 2 | 已終止 ⚠️ | 86 | Temozolomide（與 Dacarbazine 共享活性代謝物 MTIC）用於 MGMT 甲基化之晚期上呼吸消化道癌（含頭頸癌、食道癌）及大腸直腸癌——86 人入組後提前終止，整體反應率偏低，療效訊號不明確 |

> **注意**：上表試驗藥物為 Temozolomide，非 DACARBAZINE 本身。兩者共享活性代謝物 MTIC，可提供間接參考，但不能直接等同；終止狀態為重大負面訊號。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41481311](https://pubmed.ncbi.nlm.nih.gov/41481311/) | 2026 | Phase 3 RCT | JAMA Oncology | Toripalimab vs DACARBAZINE 作為晚期肢端型黑色素瘤一線治療——確認 Dacarbazine 現為黑色素瘤標準對照藥物，PD-1 抑制劑顯著優於 Dacarbazine |
| [23443801](https://pubmed.ncbi.nlm.nih.gov/23443801/) | 2013 | Phase 2（已發表結果） | Molecular Cancer Therapeutics | NCT00423150 結果：MGMT 甲基化可篩選 UADT/大腸直腸癌患者，但 Temozolomide 單藥反應率仍偏低，間接說明共享 MTIC 機轉在此適應症的侷限性 |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | 臨床研究 | Annals of Oncology | DACARBAZINE + 5-FU 組合用於晚期甲狀腺髓質癌（MTC），為 Dacarbazine 直接用於 UADT 鄰近神經內分泌腫瘤的稀少臨床紀錄 |
| [8346929](https://pubmed.ncbi.nlm.nih.gov/8346929/) | 1993 | 病例系列 | Gan to Kagaku Ryoho | CYVADIC 方案（含 DTIC/Dacarbazine）用於頭頸部老年型血管肉瘤，提供 Dacarbazine 用於頭頸部罕見惡性腫瘤的早期臨床依據 |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | 回顧性研究 | Ear, Nose & Throat Journal | 頭頸部惡性副神經節瘤 6 例分析，探討罕見 UADT 惡性腫瘤的基因突變與治療策略 |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | Review | Clinical Oncology | 甲狀腺髓質癌全面回顧，介紹化療（含 Dacarbazine 組合）在難治性 MTC 中的角色與侷限 |
| [20564093](https://pubmed.ncbi.nlm.nih.gov/20564093/) | 2010 | 回顧性研究 | Cancer | 頭頸部節外及節內霍奇金淋巴瘤特徵與預後——ABVD 方案（含 Dacarbazine）在頭頸部 HL 的療效分析 |
| [11163509](https://pubmed.ncbi.nlm.nih.gov/11163509/) | 2001 | 病例系列 | Int J Radiat Oncol Biol Phys | 嗅神經母細胞瘤（鼻腔罕見惡性腫瘤）放療分析，屬 UADT 腫瘤範疇，提供局部控制的背景資訊 |
| [25772801](https://pubmed.ncbi.nlm.nih.gov/25772801/) | 2015 | Review | J Clinical Neuroscience | Temozolomide（共享 MTIC）用於侵襲性腦垂體腫瘤，支持烷化劑於神經內分泌腫瘤的潛在療效 |
| [34705104](https://pubmed.ncbi.nlm.nih.gov/34705104/) | 2022 | 流行病學回顧 | J Cancer Res Clin Oncol | EB 病毒相關癌症全球負擔估算，部分涉及 UADT（鼻咽癌等），提供流行病學背景 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（烷化劑 / Imidazotetrazine 類） |
| 骨髓抑制風險 | 中至高度（白血球減少及血小板減少為劑量限制性毒性，通常於給藥後 2–4 週達谷值） |
| 致吐性分級 | 中至高度（靜脈給藥；建議預防性止吐） |
| 監測項目 | 全血球計數含分類（每療程前及療程中監測）、肝腎功能、基線電解質 |
| 處置防護 | 需依細胞毒性藥物處置規範操作；靜脈注射應避免外滲（具組織刺激性）；調配需在生物安全櫃中進行 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
雖然 DACARBAZINE 的 MTIC 烷化機轉對 UADT 腫瘤理論上具有合理性，但唯一相關的代謝物共享臨床試驗（Temozolomide，NCT00423150）已因療效不足提前終止，且 DACARBAZINE 在台灣無上市許可、安全性資訊缺口嚴重，現有直接臨床證據不足以支持進一步推進。

**若要推進需要：**
- 取得 DACARBAZINE 完整仿單，補足作用機轉（MOA）與安全性警語資料
- 詳細分析 NCT00423150 終止原因（療效不足 vs. 安全性問題），評估是否具有族群篩選空間
- 評估 UADT 腫瘤 MGMT 甲基化狀態的篩選策略，確認潛在受益族群比例
- 考量聯合用藥方案（如 Dacarbazine + 免疫治療），而非單藥模式
- 台灣特殊用藥申請或同情用藥途徑的法規可行性評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

