---
layout: default
title: Tiotropium
parent: 高證據等級 (L1-L2)
nav_order: 866
evidence_level: L1
indication_count: 5
---

# Tiotropium
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

# Tiotropium：從 COPD 到阻塞性肺疾病

## 一句話總結

Tiotropium 是長效型抗膽鹼支氣管擴張劑（LAMA），原本用於慢性阻塞性肺病（COPD）的維持治療。
TxGNN 模型預測它可能對**阻塞性肺疾病 (Obstructive Lung Disease)** 有效，目前有 **50 個臨床試驗**和 **20 篇文獻**支持這個方向。
但這個預測詞是 COPD 的上位概念，COPD 本來就是已知適應症，所以較接近「確認既有用途」，不是真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症文字；證據包註記 COPD 為已知適應症 |
| 預測新適應症 | 阻塞性肺疾病 (Obstructive Lung Disease) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

DrugBank 的作用機轉欄位目前沒有資料。根據證據包的機轉推論，Tiotropium 是毒蕈鹼受體拮抗劑，會阻斷氣道平滑肌上的 M3 受體，降低膽鹼性張力，產生持續的支氣管擴張。文獻指出它對 M3 和 M1 受體的解離很慢，作用時間長，可以每日一次給藥（PMID 10069510、12010082）。

阻塞性肺疾病是以氣流受阻為特徵的疾病總稱，COPD 屬於其中。Tiotropium 的機轉直接作用在氣流受阻上，所以預測在機轉上說得通。

**需要留意：** 這個預測詞涵蓋範圍很廣，與既有適應症 COPD 高度重疊，不是獨立的新適應症。要評估真正的新用途，應該看更具體的疾病子類型。

---

## 臨床試驗證據

共 50 個相關試驗，以下列出 10 個最相關的：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01012765](https://clinicaltrials.gov/study/NCT01012765) | Phase 3 | 完成 | 173 | 隨機雙盲交叉試驗，比較 Indacaterol 與安慰劑對中度 COPD 吸氣容量的影響，以開放標示 Tiotropium 為對照 |
| [NCT00277264](https://clinicaltrials.gov/study/NCT00277264) | Phase 3 | 完成 | 914 | SAFE 試驗，Tiotropium 18 mcg 每日一次，為期一年，評估 FEV1 變化是否受吸菸狀態影響 |
| [NCT00144339](https://clinicaltrials.gov/study/NCT00144339) | Phase 3 | 完成 | 5993 | 評估 Tiotropium 是否能減緩 COPD 患者肺功能的下降速率 |
| [NCT00274014](https://clinicaltrials.gov/study/NCT00274014) | Phase 3 | 完成 | 1000 | 一年期治療對中重度 COPD 肺功能及急性惡化頻率與嚴重度的影響 |
| [NCT02006732](https://clinicaltrials.gov/study/NCT02006732) | Phase 3 | 完成 | 809 | Tiotropium + Olodaterol 固定劑量複方對比單用 Tiotropium 與安慰劑，為期 12 週 |
| [NCT00523991](https://clinicaltrials.gov/study/NCT00523991) | Phase 4 | 完成 | 457 | 24 週隨機雙盲試驗，對象為未接受維持治療的 COPD 患者 |
| [NCT00776984](https://clinicaltrials.gov/study/NCT00776984) | Phase 3 | 完成 | 453 | 嚴重持續性氣喘的附加控制療法，為期 48 週（氣喘族群，非 COPD） |
| [NCT00515502](https://clinicaltrials.gov/study/NCT00515502) | Phase 2 | 完成 | 24 | 劑量遞增交叉試驗，Tiotropium 為對照藥，提供藥效學參考 |
| [NCT01112241](https://clinicaltrials.gov/study/NCT01112241) | Phase 4 | 完成 | 17 | 造血幹細胞移植後閉塞性細支氣管炎對支氣管擴張劑的急性反應（小型研究） |
| [NCT03199976](https://clinicaltrials.gov/study/NCT03199976) | Phase 4 | 提前終止 | 80 | 間歇性使用於幼兒反覆喘鳴，因族群不同且提早終止，參考價值有限 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | N Engl J Med | 研究輕中度 COPD 患者長期使用 Tiotropium，是否改善肺功能並減緩其下降 |
| [29605624](https://pubmed.ncbi.nlm.nih.gov/29605624/) | 2018 | RCT（DYNAGITO） | Lancet Respir Med | 比較 Tiotropium + Olodaterol 與單用 Tiotropium 預防 COPD 急性惡化的效果 |
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | 系統性回顧 | Cochrane Database Syst Rev | Tiotropium 對比安慰劑，作為穩定期 COPD 每日維持治療 |
| [19402836](https://pubmed.ncbi.nlm.nih.gov/19402836/) | 2009 | 統合分析 | Respirology | 評估 Tiotropium 在中國穩定期 COPD 患者的療效與安全性 |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Review | Respir Res | Tiotropium 在 COPD 的臨床開發回顧，LAMA 單一療法為 GOLD B/C/D 組的起始治療建議 |
| [33095662](https://pubmed.ncbi.nlm.nih.gov/33095662/) | 2021 | Review | Curr Med Res Opin | 回顧 Tiotropium + Olodaterol 固定劑量複方作為起始與後續治療的證據 |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | Review | Life Sci | Tiotropium 的機轉與臨床特性，受體解離緩慢而作用持久 |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | 藥物綜述 | Drugs | Tiotropium 拮抗 M1、M2、M3 受體，作用時間長，可每日一次給藥 |
| [35510163](https://pubmed.ncbi.nlm.nih.gov/35510163/) | 2022 | 觀察性（世代研究） | Int J Chron Obstruct Pulmon Dis | 台灣多中心世代研究，比較三種 LABA/LAMA 固定劑量複方的真實世界療效 |
| [36714923](https://pubmed.ncbi.nlm.nih.gov/36714923/) | 2023 | 觀察性（前瞻性） | Expert Rev Respir Med | 評估 Tiotropium 吸入劑在有症狀的中國 COPD 患者的療效與安全性 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51091 | SPIRIVA CAP FOR INHALATION 18MCG | 未載明 | 未載明 |
| HK-57639 | SPIRIVA RESPIMAT SOL FOR INHAL 2.5MCG | 未載明 | 未載明 |
| HK-50663 | SPIRIVA CAP FOR INHAL 18MCG (COMBOPACK) | 未載明 | 未載明 |
| HK-64356 | SPIOLTO RESPIMAT INHALATION SOLUTION 2.5MCG/2.5MCG | 未載明 | 未載明 |

以上許可證皆由 BOEHRINGER INGELHEIM (HK) LTD 持有。

---

## 安全性考量

目前沒有仿單層級的警語、禁忌症與藥物交互作用資料，請參考原廠仿單。

文獻中出現過以下安全訊號，推進時需要審視：
- **心血管事件**：一篇 RCT 統合分析探討 Tiotropium 與心血管不良事件的關聯（PMID 32274526）。
- **眼部影響**：前房參數與眼壓相關研究（PMID 39198799；NCT06525051）。
- **失智風險**：一項世代研究探討起始使用 Tiotropium 與失智風險的關聯（PMID 40388132）。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多個已完成的 Phase 3 隨機對照試驗，以及 NEJM 的 RCT 和 Cochrane 系統性回顧，證據等級為 L1。
- 但預測詞與既有適應症 COPD 高度重疊，這份證據主要是在確認既有用途，並非證明新適應症。

**若要推進需要：**
- 取得香港衛生署的仿單，確認警語、禁忌症與核准適應症，這是目前的阻擋性缺口。
- 查詢 DrugBank 補齊作用機轉資料。
- 逐一核對各張許可證的核准適應症與劑型，確認預測的疾病範圍是否已在標示內。
- 針對心血管、眼部與失智風險訊號，建立族群別的監測與評估方案。
- 若要找真正的新適應症，改評估更具體的疾病子類型，例如嚴重早發型 COPD（證據等級 L3，目前僅列為研究問題）。其餘預測如呼吸道畸形（L4）和 Rienhoff 症候群（L5，無機轉關聯）目前建議暫緩（Hold）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

