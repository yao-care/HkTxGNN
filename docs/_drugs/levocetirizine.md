---
layout: default
title: Levocetirizine
parent: 僅模型預測 (L5)
nav_order: 525
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Levocetirizine：預測新適應症為類風濕性關節炎 (Rheumatoid Arthritis)（證據等級 L5）。原適應症：過敏性鼻炎、血管運動性鼻炎、特發性蕁麻疹"
---

# Levocetirizine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Levocetirizine：從過敏性鼻炎到類風濕性關節炎

## 一句話總結

Levocetirizine 是第二代選擇性 H1 受體拮抗劑（抗組織胺），原本用於過敏性鼻炎、血管運動性鼻炎與慢性特發性蕁麻疹。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，這僅是模型的計算預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏性鼻炎、血管運動性鼻炎、特發性蕁麻疹（來自 TxGNN 知識圖譜；香港許可證未提供適應症文字） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Levocetirizine 是選擇性 H1 受體拮抗劑，主要在過敏性疾病中阻斷組織胺作用。

組織胺與肥大細胞活性被認為可能參與關節滑膜發炎，因此抗組織胺藥在生物學上有可能帶來抗發炎效果。不過，這個關聯目前仍屬推測。

需要特別說明：0.997 的 TxGNN 分數是計算預測，不是臨床證據。過敏性疾病與類風濕性關節炎（自體免疫疾病）的病理機轉差異很大，缺乏實際研究佐證。

另外兩個排名靠前的預測為「colobomatous microphthalmia-rhizomelic dysplasia syndrome」（分數 99.59%）與「brachydactyly-syndactyly syndrome」（分數 99.52%）。兩者皆為先天性遺傳或發育異常，H1 受體拮抗無法合理解釋其療效，應視為知識圖譜的偽陽性，不建議進一步投入。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 20 張有效的單方許可證，以下列出 5 張主要許可證（許可證資料未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-49629 | XYZAL TAB 5MG（GlaxoSmithKline） | 錠劑 5mg | 未提供 |
| HK-54600 | XYZAL ORAL DROPS 5MG/ML（GlaxoSmithKline） | 口服滴劑 | 未提供 |
| HK-58738 | ALCET TAB 5MG（Deltapharm） | 錠劑 5mg | 未提供 |
| HK-63098 | XYLACLEAR TABLETS 5MG（Sino Pacific Pharma） | 錠劑 5mg | 未提供 |
| HK-63096 | XYLACLEAR ORAL SOLUTION 0.5MG/ML（Sino Pacific Pharma） | 口服溶液 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的疾病禁忌**（來自 TxGNN 知識圖譜，非仿單內容）：腎臟疾病、慢性腎臟病、慢性腎衰竭症候群、末期腎衰竭、輸尿管積膿。Levocetirizine 主要經腎臟排除，腎功能不全患者需特別留意。
- **藥物交互作用**：資料庫共記錄 100 筆交互作用，以下為部分中度（Moderate）者：
  - 中樞神經抑制類：Morphine、Fentanyl、Dihydrocodeine、Opium、Ethanol、Promethazine、Chlorpheniramine
  - 止瀉／腸胃藥：Loperamide、Diphenoxylate、Difenoxin、Metoclopramide
  - 其他：Bupropion、Dronabinol、Nabilone、Sibutramine、Histamine、Iodide I-131、Iodide I-123
  - Hyaluronidase 為輕微（Minor）等級

  合併使用中樞抑制劑時，須留意嗜睡與鎮靜加成效應。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 三個預測適應症皆無臨床試驗與文獻支持，證據等級僅為 L5。
- 類風濕性關節炎的機轉連結仍屬推測；另外兩個預測缺乏合理的機轉解釋。

**若要推進需要：**
- 取得作用機轉（MOA）資料，並系統性檢索抗組織胺藥於類風濕性關節炎的前臨床與臨床文獻
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性篩選
- 評估腎功能不全族群的劑量與風險
- 若文獻回顧顯示有合理訊號，再設計探索性研究（如動物模型或小型 Phase 2 試驗）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

