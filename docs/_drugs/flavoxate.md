---
layout: default
title: Flavoxate
parent: 僅模型預測 (L5)
nav_order: 378
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Flavoxate：預測新適應症為注意力不足過動症（無注意力不足型）(Attention Deficit Hyperactivity Disorder…（證據等級 L5）。原適應症：香港許可證資料未載明適應症文字"
monitor_inn: "Flavoxate"
predicted_indications: ["attention deficit hyperactivity disorder, inattentive type", "irritable bowel syndrome", "specific developmental disorder", "attention deficit-hyperactivity disorder", "cauda equina syndrome", "obsolete neurogenic bladder (disease)", "gastroduodenitis", "peptic ulcer disease"]
---

# Flavoxate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Flavoxate：從泌尿道痙攣症狀到腸躁症（預測）

## 一句話總結

Flavoxate 是一種泌尿道抗痙攣藥物，香港目前有 2 張有效的單一成分許可證。
TxGNN 模型預測它可能對**腸躁症 (Irritable Bowel Syndrome)** 有效（預測分數 99.74%），這是機轉上最合理的預測之一。
不過目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測（證據等級 L5）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明適應症文字 |
| 預測新適應症 | 注意力不足過動症（無注意力不足型）(Attention Deficit Hyperactivity Disorder, Inattentive Type)，為模型排名第 1 的預測；另有 7 項預測（見下方） |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

**所有預測適應症一覽：**

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 1 | 注意力不足過動症（無注意力不足型） | 99.75% | L5 | Hold |
| 2 | 腸躁症 (Irritable Bowel Syndrome) | 99.74% | L5 | Hold |
| 3 | 特定發展障礙 (Specific Developmental Disorder) | 99.56% | L5 | Hold |
| 4 | 注意力不足過動症 (ADHD) | 99.39% | L5 | Hold |
| 5 | 馬尾症候群 (Cauda Equina Syndrome) | 99.27% | L5 | Hold |
| 6 | 神經性膀胱（已過時術語） | 99.13% | L5 | Hold |
| 7 | 胃十二指腸炎 (Gastroduodenitis) | 99.12% | L5 | Hold |
| 8 | 消化性潰瘍 (Peptic Ulcer Disease) | 99.10% | L5 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據一般藥理認識，Flavoxate 是泌尿道抗痙攣藥，具有平滑肌鬆弛、磷酸二酯酶抑制及微弱抗膽鹼作用，但這些描述並非來自本報告所整理的資料，仍需以正式資料確認。

各預測的合理性差異很大：

- **腸躁症（排名 2）**：平滑肌鬆弛與抗膽鹼作用正是現有腸道抗痙攣藥用於腸躁症的基礎，機轉上有道理，但缺乏 Flavoxate 本身的試驗或文獻，仍未經驗證。
- **神經性膀胱（排名 6）**：Flavoxate 對逼尿肌的抗痙攣作用與膀胱過動、尿急相關，與現有泌尿道用途接近，較像現有適應症的延伸而非真正的再利用。此疾病術語已過時，後續應對應到現行術語（如神經源性逼尿肌過動）。
- **ADHD 相關（排名 1、3、4）**：沒有任何資料支持其機轉。多個高分 ADHD 與神經發展相關預測同時出現，可能反映知識圖譜的共同關聯，而非獨立訊號。
- **馬尾症候群（排名 5）**：最多只能緩解膀胱痙攣或尿急症狀，無法處理根本的神經壓迫（屬外科急症）。
- **胃十二指腸炎、消化性潰瘍（排名 7、8）**：缺乏對黏膜發炎或胃酸分泌的作用證據；Flavoxate 抗膽鹼作用微弱，標準治療為抑酸與根除幽門螺旋桿菌。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65106 | FUCOTIN TABLETS 200MG（Hitpharm Pharmaceutical Co Ltd） | 錠劑（品名標示） | 資料未載明 |
| HK-54672 | FOXATE F.C. TAB 200MG（Synmosa Biopharma (Hong Kong) Company Limited） | 膜衣錠（品名標示） | 資料未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病禁忌關聯，非仿單內容）：閉角型青光眼、幽門狹窄、麻痺性腸阻塞、腸阻塞、家族性內臟肌病變、活動性消化性潰瘍、泌尿道阻塞。
  - 值得注意：預測適應症中的「消化性潰瘍」與知識圖譜中的「活動性消化性潰瘍」禁忌互相衝突，這進一步降低該預測的可行性。
- **藥物交互作用**：共查得 74 筆，以下為本次資料中列出的主要項目：
  - **重大 (Major)**：Potassium citrate、Potassium chloride
  - **中度 (Moderate)**：多種抗膽鹼／抗痙攣藥（Hyoscyamine、Atropine、Glycopyrronium、Clidinium、Dicyclomine、Trospium、Mepenzolate、Methscopolamine、Propantheline、Scopolamine），以及 Loperamide、Morphine、Dronabinol、Nabilone、Eluxadoline、Metoclopramide、Pramlintide、Prucalopride
- 仿單的主要警語與禁忌症資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 8 項預測皆僅有模型分數支持，沒有臨床試驗與文獻，證據等級均為 L5。
- 香港許可證缺少適應症與仿單安全資料，且存在知識圖譜禁忌關聯（尤其與消化性潰瘍預測衝突），目前不足以推進。

**若要推進需要：**
- 取得香港衛生署仿單，確認原適應症、警語與禁忌症
- 補齊作用機轉（MOA）資料，例如從 DrugBank 取得
- 優先針對**腸躁症**與**神經性膀胱**（改用現行術語）進行系統性文獻與試驗檢索
- 在 ADHD 相關預測投入資源前，先檢查是否為圖譜假象
- 若進入腸躁症評估，需評估抗膽鹼類藥物重複使用的風險，以及上述禁忌疾病族群的排除標準
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

