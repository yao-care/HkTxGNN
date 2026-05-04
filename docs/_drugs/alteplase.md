---
layout: default
title: Alteplase
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 9
---

# Alteplase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# ALTEPLASE：從急性血栓栓塞治療到後外側心肌梗塞

## 一句話總結

ALTEPLASE（rtPA，重組組織型纖溶酶原激活劑）是臨床上廣泛使用的血栓溶解藥物，已知用於急性缺血性腦中風、肺栓塞及 STEMI 的急性期治療。TxGNN 模型預測它可能對**後外側心肌梗塞（Posterolateral Myocardial Infarction）** 具有獨立研究價值，目前有 **0 個臨床試驗**和 **3 篇間接文獻**支持此方向——預測反映的是此特定解剖亞型尚未被系統研究的知識缺口，而非藥物機轉的新穎性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性缺血性腦中風、肺栓塞、急性心肌梗塞（STEMI）溶栓治療（Evidence Pack 未提供，依已知藥理） |
| 預測新適應症（排名 #1） | 後外側心肌梗塞（Posterolateral Myocardial Infarction） |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L4（前臨床/間接文獻支持，無直接 RCT） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Research Question |

---

## 為什麼這個預測合理？

Alteplase 是重組組織型纖溶酶原激活劑（recombinant tissue-type plasminogen activator，rtPA），其核心機轉為：與纖維蛋白結合後將纖溶酶原（plasminogen）活化為纖溶酶（plasmin），進而降解血栓中的纖維蛋白網絡，恢復閉塞血管的血流。此作用具纖維蛋白特異性，是目前 STEMI 急性溶栓的重要選項之一。本 Evidence Pack 中 MOA 詳細資料標記為缺失，以上機轉說明來自已發表藥理文獻。

後外側心肌梗塞（Posterolateral MI）主要由左迴旋支（LCx）或後降支（PDA）急性血栓性閉塞所致，其病理核心——冠狀動脈內血栓形成——與 alteplase 現有適應症（STEMI）完全一致。現有文獻（PMID 9502627）已顯示，在急性下壁 MI 患者中，後胸導聯（V7–V9）ST 段抬高可識別合併後壁梗塞的亞型，且此群體可能從溶栓治療中獲益更多，機轉合理性有初步佐證。

然而，「後外側」作為 MI 的具體解剖分型，目前尚缺乏針對性的 RCT 或 Phase 1/2 試驗，既有大型溶栓試驗（如 TAMI、GUSTO 系列）均以整體 STEMI 為研究對象，未做此亞型的獨立分析。TxGNN 的預測，很可能反映的是知識圖譜中此亞型尚未被系統研究的知識缺口，而非全新的治療假說。

---

## 臨床試驗證據

目前無針對後外側心肌梗塞（Posterolateral Myocardial Infarction）的相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9502627](https://pubmed.ncbi.nlm.nih.gov/9502627/) | 1998 | 觀察性研究 | J Am Coll Cardiol | 後胸導聯（V7–V9）ST 抬高可識別急性下壁 MI 合併後壁梗塞的患者；此亞群可能較單純下壁 MI 更受益於溶栓治療，為後壁梗塞溶栓提供間接依據 |
| [8480981](https://pubmed.ncbi.nlm.nih.gov/8480981/) | 1993 | 案例報告 | Ann Cardiol Angiol | 後外側 MI 患者接受 tPA 晚期溶栓期間，發生快速消退的腦栓塞 1 例；文獻回顧 MI 急性期纖溶治療與左心室血栓及全身栓塞的相關風險，提示安全性監測需求 |
| [21351226](https://pubmed.ncbi.nlm.nih.gov/21351226/) | 2011 | 案例報告/介入報告 | Catheter Cardiovasc Interv | 37 歲男性後外側急性 MI 合併左主幹閉塞（EF 30%），急診 PCI 過程中輔助冠狀動脈內 reteplase（tPA 同類藥），成功實現再灌注，提示 tPA 類藥物在此亞型複雜解剖情境的可行性 |

---

## 香港上市資訊

ALTEPLASE 目前在香港**無藥物許可證登記**，屬未上市藥物。如有臨床使用需求，須依香港衛生署相關法規申請特別進口許可。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **提示**：ALTEPLASE 為靜脈注射用溶栓藥物，出血風險（含顱內出血）為已知主要不良事件，臨床使用需嚴格評估禁忌症（如近期手術、出血性疾病等）。本 Evidence Pack 未提供詳細警語及禁忌資料，請務必查閱原廠說明書。

---

## 其他預測適應症概覽

以下為本次 TxGNN 評估的全部 9 個預測適應症摘要，供研究優先序規劃參考：

| 排名 | 適應症 | TxGNN 分數 | 臨床試驗 | 文獻 | 證據等級 | 建議決策 |
|------|--------|-----------|---------|------|---------|---------|
| 1 | 後外側心肌梗塞（Posterolateral MI） | 99.79% | 0 | 3 | L4 | Research Question |
| 2 | 後下壁心肌梗塞（Posteroinferior MI） | 99.79% | 0 | 1 | L4 | Hold |
| 3 | 室間隔心肌梗塞（Septal MI） | 99.77% | 1 | 13 | L3 | Research Question |
| 4 | 肝素輔因子 2 缺乏症（HC2 Deficiency） | 99.72% | 0 | 20 | L4 | Research Question |
| 5 | 先天性冠狀動脈異常（Congenital Coronary Anomaly） | 99.64% | 4 | 5 | L4 | Research Question |
| 6 | 第五凝血因子過量合併自發性血栓 | 99.56% | 0 | 0 | L5 | Hold |
| 7 | 抗凝血酶缺乏症 2 型（AT Deficiency Type 2） | 99.56% | 0 | 0 | L5 | Hold |
| **8** | **血栓形成傾向（Thrombophilia）** | **99.43%** | **9** | **20** | **L3** | **Proceed with Guardrails** |
| 9 | 冠狀動脈狹窄（Coronary Stenosis） | 99.14% | 7 | 20 | L3 | Research Question |

> **研究優先建議**：排名 #8「血栓形成傾向（Thrombophilia）」雖 TxGNN 分數略低，但擁有最充分的臨床試驗支持（9 個，含 Phase 2 直接評估 tPA 的 NCT05540834 及 n=209 的 RCT NCT00251771），建議作為優先研究方向。

---

## 結論與下一步

**決策：Research Question（針對首要預測：後外側心肌梗塞）**

**理由：**
Alteplase 在機轉上完全適用於後外側 MI（LCx/PDA 血栓性閉塞），但此特定解剖亞型缺乏直接的臨床試驗資料；現有大型溶栓試驗未對此亞型進行獨立分析，尚不足以支撐直接進入臨床研究規劃，需先確立研究假說的獨特性與必要性。

**整體組合中，最具推進潛力的方向為「血栓形成傾向（Thrombophilia，排名 #8）」**，建議以 Proceed with Guardrails 策略優先評估：已有 Phase 2 隨機試驗主動評估 VET 引導的 tPA 劑量（NCT05540834），且導管定向靜脈溶栓的 RCT（NCT00251771，n=209）提供直接療效依據。

**若要推進後外側 MI 的研究需要：**
- 補充 ALTEPLASE 完整的官方核准適應症清單（原廠仿單或 DrugBank API 查詢）
- 補充詳細 MOA 資料，建立與 STEMI 亞型之間的機轉對照分析
- 系統性回顧現有 STEMI 大型試驗（GUSTO、TAMI 系列）中後壁/後外側亞組資料
- 評估是否有必要設計後外側 MI 亞型特定的溶栓 vs. 直接 PCI 對照試驗，或在現有 STEMI 試驗中加入後壁亞型分析
- 補充香港/台灣藥監局安全性警語資料（現為資料缺口），評估在未上市地區使用的監管路徑
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

