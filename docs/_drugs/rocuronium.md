---
layout: default
title: Rocuronium
parent: 僅模型預測 (L5)
nav_order: 768
evidence_level: L5
indication_count: 10
---

# Rocuronium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Rocuronium：從神經肌肉阻斷劑到偏頭痛

## 一句話總結

Rocuronium 是非去極化型神經肌肉阻斷劑，臨床上用於麻醉時的肌肉鬆弛。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，但目前只有 **1 個臨床試驗**（與偏頭痛無關）和 **0 篇文獻**，實質上僅有模型預測，**沒有任何證據支持這個方向**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症；藥理類別為神經肌肉阻斷劑 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位尚未取得）。根據已知藥理，Rocuronium 是非去極化型神經肌肉阻斷劑，作用於運動終板的菸鹼型乙醯膽鹼受體 (nicotinic ACh receptor) 並拮抗之。它沒有已知的中樞神經或三叉神經血管系統作用。

以機轉來看，這個預測**缺乏合理性**。偏頭痛的病理與三叉神經血管活化、CGRP 路徑等有關，與骨骼肌的神經肌肉接合處無關。此外，Rocuronium 使用時必須有呼吸支持，不適合用於慢性、發作性的疾病。

TxGNN 給出 99.90% 的高分，最可能是知識圖譜中節點相鄰造成的假象 (knowledge-graph artifact)，而非真正的藥理關聯。這個分數不應被視為療效訊號。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | 完成 | 3,520 | 兒童標準治療下「研究不足藥物」的藥物動力學研究。並未測試 Rocuronium 對偏頭痛的效果，無療效訊號（相關性：C） |

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67201 | ROCURONIUM BROMIDE SOLUTION FOR INJECTION/INFUSION 50MG/5ML | MAIN LIFE CORP LTD |
| HK-64818 | ROCURONIUM KABI SOLUTION FOR INJECTION/INFUSION 50MG/5ML | FRESENIUS KABI HONG KONG LIMITED |
| HK-59706 | ROCURONIUM SOLUTION FOR INJ 10MG/ML | MEKIM LTD |
| HK-67000 | ROCURONIUM B. BRAUN SOLUTION FOR INJECTION/INFUSION 50MG/5ML | B. BRAUN MEDICAL (HK) LTD |
| HK-67219 | ROCURONIUM BROMIDE KALCEKS SOLUTION FOR INJECTION/INFUSION 50MG/5ML | SB PHARMA LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5，只有模型預測，唯一的臨床試驗與偏頭痛無關。
- 機轉上沒有合理的關聯。其他排名靠前的預測也呈現同樣情形，包括 migraine with brainstem aura、cauda equina syndrome、irritable bowel syndrome 等，全部是 Hold，且機轉均不成立。
- 排名第 10 的 headache disorder 雖有 L4 證據，但內容是麻醉或電痙攣治療 (ECT) 後頭痛屬於術後不良反應，並非 Rocuronium 治療頭痛。

**若要重新評估需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症資料。
- 從 DrugBank 補齊作用機轉 (MOA)。
- 人工複核知識圖譜中 Rocuronium 到偏頭痛的連結路徑，確認是否為假象。
- 出現以 Rocuronium 治療偏頭痛或頭痛的直接臨床或前臨床研究後，再重新啟動評估。

> 本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

