---
layout: default
title: Inclisiran
parent: 中證據等級 (L3-L4)
nav_order: 395
evidence_level: L3
indication_count: 10
---

# Inclisiran
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

# Inclisiran：從家族性高膽固醇血症到主動脈畸形（初步假說）

## 一句話總結

Inclisiran 是一款標靶 PCSK9 的 siRNA 藥物，用於降低 LDL 膽固醇（相關臨床試驗顯示其核心族群為家族性高膽固醇血症患者）。
TxGNN 模型列出的前 10 個預測適應症中，**多數（含分數最高的 "potassium deficiency disease"）已被證據審查判定為知識圖譜嵌入雜訊**，唯一具備實際臨床試驗證據的是 **主動脈畸形 (Aortic Malformation)**，目前有 **2 個 Phase 3 臨床試驗**，但機轉關聯性與試驗收案條件仍需人工核實。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 家族性高膽固醇血症／高 LDL 膽固醇血症（依國際臨床試驗脈絡推斷；香港無核准適應症紀錄） |
| 預測新適應症 | 主動脈畸形 (Aortic Malformation) |
| TxGNN 預測分數 | 99.76%（rank 5213） |
| 證據等級 | L3 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Inclisiran 透過 siRNA 機轉抑制 PCSK9 基因表現，減少 PCSK9 蛋白對肝臟 LDL 受體的降解，進而提升 LDL-C 清除能力，屬於脂質代謝路徑的標靶藥物。目前尚缺乏 DrugBank 完整 MOA 描述（DG002，High severity data gap），以上機轉資訊係由本評估團隊依臨床試驗脈絡整理，非官方仿單資料。

**主動脈畸形的機轉關聯性偏弱**：主動脈結構性畸形（如主動脈弓發育缺陷、Marfan 症候群相關病變）主要成因為結締組織／血管發育異常，與 PCSK9/LDL 代謝路徑並無已知直接分子關聯。支持此預測的 2 個 Phase 3 試驗（NCT06597006、NCT06597019）標題僅顯示「Inclisiran vs Placebo」之通用降脂設計，且收案對象為 2–12 歲兒童之同型合子／異型合子家族性高膽固醇血症（HoFH/HeFH）患者，enrollment 極小（9 人、51 人），高度懷疑是**罕見遺傳性高膽固醇血症合併血管結構病變之利基族群**，而非以「主動脈畸形」本身作為治療標的——換言之，這很可能是**疾病本體詞彙映射（ontology mapping）誤差**，需人工核實試驗實際收案條件後才能確認證據等級是否成立。

**其餘 9 個預測適應症的證據品質不足以支持假說**：
- Rank 1、2、3、5、6、9、10（potassium deficiency disease、esophageal disease、atypical coarctation of aorta、non-syndromic esophageal malformation、migraine with brainstem aura、esophageal ulcer、Raynaud disease）：零臨床試驗、零文獻，且各自機轉分析均判定為**知識圖譜嵌入之高分雜訊**，非真實生物學假說。
- Rank 4（migraine disorder）：零試驗、零文獻，僅有極薄弱的理論連結（他汀類藥物脂質調控假說），無法外推至 siRNA 機轉。
- Rank 7（migraine with or without aura, susceptibility to）：雖有 20 篇文獻，但內容集中於癲癇／偏頭痛易感基因研究（如 SCN1A、MTHFR C677T 多型性），屬**疾病本身的遺傳學文獻**，並未涉及 Inclisiran 或 PCSK9 路徑，屬於「疾病共病文獻」被誤判為「藥物-疾病證據」的典型情形。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06597006](https://clinicaltrials.gov/study/NCT06597006) | Phase 3 | Recruiting | 9 | 評估 Inclisiran 在 2–12 歲同型合子家族性高膽固醇血症（HoFH）合併 LDL-C 升高兒童之安全性、耐受性與療效（Year 1 雙盲 vs 安慰劑，Year 2 開放標籤）；未明示以主動脈畸形為治療標的，需核實實際收案條件 |
| [NCT06597019](https://clinicaltrials.gov/study/NCT06597019) | Phase 3 | Recruiting | 51 | 姊妹試驗，對象為 6–12 歲異型合子家族性高膽固醇血症（HeFH）合併 LDL-C 升高兒童，設計與上者相同，同樣缺乏明確之主動脈畸形適應症敘述 |

---

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

Inclisiran 目前**未在香港上市**，無核准許可證紀錄（total_licenses = 0）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：TFDA／香港仿單警語與禁忌症資料為 Blocking 等級資料缺口（DG001），現階段**無法完成 S1 安全性初評**，此為推進本候選前必須補齊的關鍵資料。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 分數最高的多個預測適應症經證據審查後判定為模型雜訊，不具生物學合理性；唯一有試驗支持的「主動脈畸形」機轉關聯薄弱，且高度懷疑為疾病本體詞彙映射誤差，需先核實試驗實際收案條件與主要療效指標。
- 藥物尚未在香港上市，且仿單警語／禁忌症資料缺失（Blocking data gap），無法完成基本安全性初評，暫不具備推進條件。

**若要推進需要：**
- 查證 NCT06597006、NCT06597019 之實際 inclusion criteria 與主要療效指標，確認是否真的涉及主動脈畸形適應症，或僅為 HoFH/HeFH 合併血管病變之利基族群試驗
- 取得 TFDA／香港仿單完整警語與禁忌症資料，完成 S1 安全性初評（DG001）
- 取得 Inclisiran 詳細作用機轉（MOA）官方資料，強化機轉關聯性分析（DG002）
- 若無明確上市計畫，需重新評估本候選在香港市場的適用性與優先順序
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

