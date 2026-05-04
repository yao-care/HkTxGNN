---
layout: default
title: Ciprofloxacin
parent: 中證據等級 (L3-L4)
nav_order: 141
evidence_level: L4
indication_count: 10
---

# Ciprofloxacin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Ciprofloxacin：從廣效抗生素到瀰漫性硬皮病

## 一句話總結

Ciprofloxacin 是氟喹諾酮類廣效抗生素，長期用於多種細菌感染的治療。
TxGNN 模型預測它可能對**瀰漫性硬皮病 (Diffuse Scleroderma)** 有潛在療效，
目前有 **0 個臨床試驗**和 **2 篇文獻**支持這個方向，整體證據基礎薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 廣效抗生素（細菌感染治療） |
| 預測新適應症 | 瀰漫性硬皮病 (Diffuse Scleroderma) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Ciprofloxacin 是第三代氟喹諾酮類廣效抗生素，其作用機轉為抑制細菌的 DNA gyrase（促旋酶）與 Topoisomerase IV，阻斷細菌 DNA 複製與修復，達到殺菌效果。本 Evidence Pack 未提供正式 MOA 資料，上述資訊源自公開藥理學文獻；若需正式記錄，建議查詢 DrugBank API（DB00537）補全。

TxGNN 模型對此預測提出**雙重機轉假說**：

1. **抗纖維化特性**：體外研究顯示 Ciprofloxacin 可能抑制 TGF-β 相關訊號通路，進而減少膠原蛋白過度沉積。瀰漫性硬皮病（系統性硬化症，SSc）的核心病理即為皮膚及內臟的進行性纖維化，若此機轉在體內成立，將提供一合理的生物學連結。

2. **腸道細菌過生長（SIBO）介導路徑**：SSc 患者常因腸道運動功能障礙而併發小腸細菌過生長，氟喹諾酮類（含 Ciprofloxacin）可有效清除過生長細菌，間接改善 GI 症狀及系統性炎症反應，可能對整體疾病表現產生影響。

然而，上述兩條路徑目前均缺乏大型臨床驗證，屬於機轉層級的推論，機轉尚未確立，需謹慎對待。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Clinical Pilot Study | The Journal of Dermatology | 雙盲隨機臨床試驗探討口服 Ciprofloxacin 能否降低硬皮病皮膚纖維化嚴重程度，為目前最直接的臨床試驗性證據 |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Observational/Diagnostic Study | British Journal of Rheumatology | 24 名系統性硬化症患者小腸細菌過生長的診斷與抗菌治療結果研究，支持 SIBO 介導路徑假說 |

---

## 香港上市資訊

根據本 Evidence Pack，Ciprofloxacin 在香港目前登記為**未上市**，無任何有效許可證紀錄。如需進一步確認，建議直接查詢香港衛生署藥物辦公室資料庫。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意事項**：根據 Evidence Pack 預測排名，Rank 9（伴發周圍神經病變的血液疾病）有特殊安全性疑慮——Ciprofloxacin 本身的 FDA Black Box Warning 即包含周圍神經病變風險，在已有此類症狀的患者中使用需特別謹慎。

---

## 結論與下一步

**決策：Hold**

**理由：**
目前針對瀰漫性硬皮病僅有 2 篇低等級文獻（Level 4：前臨床/機轉研究層級），無任何已登記或進行中的臨床試驗，雙重機轉假說尚未獲得體內或大型臨床數據驗證，證據量不足以支持進一步推進。

**若要推進需要：**
- 補全正式 MOA 資料（建議查詢 DrugBank DB00537）
- 取得正式安全性資料（仿單警語、禁忌症）
- 確認抗纖維化（TGF-β 通路抑制）的前臨床證據強度與物種外推性
- 評估啟動 Ciprofloxacin 治療 SSc 的 Phase 1 探索性試驗的可行性
- 確認香港監管申請路徑（目前未上市，需考量申請許可證的可行性）

---

> **附記：更高強度的次要預測**
>
> 本 Evidence Pack 中，**Rank 10（敗血型鼠疫，Septicemic Plague）** 擁有遠更強的臨床證據支撐（L2 等級，建議 Proceed with Guardrails），包含 1 項已完成的 Phase 2 非劣效性 RCT（NCT01243437，n=200）及 2 項 RCT 方案（IMASOY，PMIDs 32807214、38970065、40768716），且 WHO、美國 CDC 均認可氟喹諾酮類作為鼠疫替代一線治療。若需就 Ciprofloxacin 最具臨床意義的再利用方向撰寫後續報告，建議以敗血型鼠疫為優先。

---

*本報告僅供研究參考，不構成醫療建議。所有老藥新用候選均需經過完整臨床驗證方可應用。*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

