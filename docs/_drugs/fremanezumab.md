---
layout: default
title: Fremanezumab
parent: 中證據等級 (L3-L4)
nav_order: 336
evidence_level: L3
indication_count: 2
---

# Fremanezumab
{: .fs-9 }

證據等級: **L3** | 預測適應症: **2** 個
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

# Fremanezumab：從偏頭痛預防到腦幹先兆型偏頭痛

## 一句話總結

Fremanezumab 是一種針對 CGRP（降鈣素基因相關肽）的全人源化單株抗體，已在慢性及發作性偏頭痛預防治療中取得 Phase 3 RCT 支持。
TxGNN 模型預測它可能對**腦幹先兆型偏頭痛 (Migraine with Brainstem Aura)** 有效，
目前有 **0 個臨床試驗**和 **20 篇文獻**（涵蓋 CGRP 通路與先兆機轉）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 偏頭痛預防（慢性偏頭痛 / 發作性偏頭痛） |
| 預測新適應症 | 腦幹先兆型偏頭痛 (Migraine with Brainstem Aura) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市（0 張許可證） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Fremanezumab 是一種全人源化 IgG2Δa 單株抗體，靶向 CGRP 本身（而非其受體）。CGRP 在三叉神經血管激活時大量釋放，是偏頭痛病理生理的核心介質。Fremanezumab 透過中和游離 CGRP，阻斷其與受體結合，進而抑制三叉神經的外周敏感化過程。目前缺乏正式的 MOA 文件資料，以上機轉描述係依據文獻及 DrugBank 類別推導而來。

腦幹先兆型偏頭痛（舊稱基底型偏頭痛，ICHD-3 代碼 1.2.2）是偏頭痛的特殊亞型，症狀源自腦幹或雙側大腦皮質，與基底動脈供血區神經活動異常有關。皮質擴散抑制（Cortical Spreading Depression, CSD）被認為是先兆的電生理基礎。動物模型顯示，fremanezumab 可延緩 CSD 的傳播速度、縮短皮質恢復期（PMID 31895266），但無法完全阻斷 CSD 的發生（PMID 31127003），提示其對先兆本身的直接干預有限。

由於腦幹先兆型偏頭痛本質上仍屬偏頭痛亞型，其三叉神經血管 CGRP 通路的核心角色與一般偏頭痛相似，機轉推斷具有合理性。然而，現有 Phase 3 RCT 均以慢性/發作性偏頭痛整體族群為對象，尚未對腦幹先兆亞型進行分層驗證，直接臨床試驗證據仍付之闕如。

---

## 臨床試驗證據

目前無相關臨床試驗登記（針對腦幹先兆型偏頭痛此特定適應症，查詢 ClinicalTrials.gov 及 ICTRP 均無結果）。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [35302681](https://pubmed.ncbi.nlm.nih.gov/35302681/) | 2022 | Post-hoc (Phase 3b) | Eur J Neurol | FOCUS 研究後驗分析：fremanezumab 對有/無先兆或神經功能異常亞組均顯示療效與生活品質改善 |
| [31895266](https://pubmed.ncbi.nlm.nih.gov/31895266/) | 2020 | Preclinical | Pain | Fremanezumab 可延緩 CSD 傳播速度、縮短皮質恢復期，但無法阻止 CSD 發生；為先兆機轉的直接動物證據 |
| [31127003](https://pubmed.ncbi.nlm.nih.gov/31127003/) | 2019 | Preclinical | J Neurosci | CSD 誘導的動脈擴張與血漿蛋白滲出不受 fremanezumab 影響，揭示 CGRP 拮抗對先兆血管反應的作用侷限 |
| [28642283](https://pubmed.ncbi.nlm.nih.gov/28642283/) | 2017 | Preclinical | J Neurosci | Fremanezumab 選擇性抑制三叉神經血管神經元，確立其周邊抑制機轉 |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case Report + Review | J Clin Med | Anti-CGRP mAbs 對偏頭痛先兆可能有預防效果，但現有文獻數量稀少 |
| [38332541](https://pubmed.ncbi.nlm.nih.gov/38332541/) | 2024 | Observational | CNS Neurosci Ther | 觀察性案例系列：anti-CGRP 標靶治療對偏頭痛先兆的預防效果初步評估 |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Individual Patient Analysis | J Headache Pain | Anti-CGRP mAbs 用於偏癱型偏頭痛（運動先兆亞型）的個別病人定量分析，顯示初步療效 |
| [40264646](https://pubmed.ncbi.nlm.nih.gov/40264646/) | 2025 | Case Report + Review | Front Neurol | Anti-CGRP mAbs 用於偏癱型偏頭痛的案例報告與文獻回顧，提示在先兆亞型中的應用潛力 |
| [35775208](https://pubmed.ncbi.nlm.nih.gov/35775208/) | 2022 | Observational | Cephalalgia | Erenumab、fremanezumab、galcanezumab 對偏頭痛中樞症狀（含先兆相關神經及精神症狀）的影響 |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handb Exp Pharmacol | CGRP 在偏頭痛（含先兆亞型）病理生理中角色的權威綜述 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Fremanezumab 在偏頭痛（慢性及發作性）已有完整的 Phase 3 RCT 支持，CGRP 通路在腦幹先兆型偏頭痛的機轉推斷具有合理性，動物模型（CSD 減速）及先兆亞組的後驗分析提供初步間接支持，但目前針對此特定亞型尚無前瞻性臨床試驗，證據等級仍止於 L3。

**若要推進需要：**
- 規劃包含腦幹先兆型偏頭痛患者（ICHD-3 1.2.2）的前瞻性隊列研究或擴展性案例系列
- 補充完整 MOA 資料（DrugBank API 查詢 DB14041）及香港仿單安全性警語
- 評估香港此罕見亞型的患者族群規模與臨床診斷實踐（需神經科轉介資料）
- 特別評估此亞型的安全顧慮：歷史上腦幹先兆患者對部分血管活性藥物有額外風險疑慮，應確認 anti-CGRP mAb 在此族群的風險效益輪廓
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

