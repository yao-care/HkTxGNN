---
layout: default
title: Diiodohydroxyquinoline
parent: 僅模型預測 (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Diiodohydroxyquinoline：預測新適應症為骨放射壞死 (Osteoradionecrosis)（證據等級 L5）。原適應症：阿米巴病（Amebiasis"
monitor_inn: "Diiodohydroxyquinoline"
predicted_indications: ["osteoradionecrosis", "radiodermatitis", "pneumonitis", "aspiration pneumonia (disease)", "type 2 diabetes nephropathy", "byssinosis", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "mixed mineral dust pneumoconiosis", "mixed dust pneumoconiosis", "Caplan syndrome"]
---

# Diiodohydroxyquinoline
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

# Diiodohydroxyquinoline：從阿米巴病到骨放射壞死

## 一句話總結

Diiodohydroxyquinoline 原本用於治療阿米巴病（腸阿米巴 *Entamoeba histolytica* 感染）。
TxGNN 模型預測它可能對**骨放射壞死 (Osteoradionecrosis)** 有效，但目前**沒有臨床試驗和文獻**支持這個預測，僅屬於模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 阿米巴病（Amebiasis；*Entamoeba histolytica* 所致） |
| 預測新適應症 | 骨放射壞死 (Osteoradionecrosis) |
| TxGNN 預測分數 | 97.96% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Diiodohydroxyquinoline 屬於 8-hydroxyquinoline 類化合物，在阿米巴病中作為腸道內抗原蟲藥物使用，機轉上是否適用於骨放射壞死尚無資料可以確認。

一個可能但未經驗證的假說是：此類化合物具有金屬（如鐵）螯合活性，或許會影響氧化壓力與纖維化過程，而這些過程與放射線造成的組織損傷有關。但這只是推測，本報告所整理的資料中沒有任何支持證據。

原適應症（腸道寄生蟲感染）與新適應症（放射線引起的骨壞死）在疾病性質上差異很大，兩者的關聯性目前無法從現有資料建立。0.98 的分數應視為計算模型的輸出，不代表已有療效證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

（備註：在其他預測適應症中，肺炎 (Pneumonitis) 有 1 篇 2020 年的藥物篩選研究 PMID 32473310，將本藥列為潛在 COVID-19 候選藥物，屬前臨床篩選，與骨放射壞死無直接關係。）

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43469 | ANLINA VAGINAL TAB | 陰道錠（依品名判斷） | 資料未提供 |

製造商：DELTAPHARM LIMITED；狀態：有效（單方）。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜的藥物－疾病關聯，非仿單文字）：肝臟疾病、膽囊疾病、腎上腺皮質功能不全 (Addison 病)、周邊神經系統疾病與周邊神經病變、視神經炎、皮膚萎縮、微血管擴張與遺傳性出血性微血管擴張症、周邊血管疾病（含間歇性跛行、周邊動脈疾病）。
- **藥物交互作用**：共查得 58 筆，以下為部分中度 (Moderate) 交互作用：
  - 抗微生物藥：Metronidazole、Tinidazole、Secnidazole、Benznidazole、Chloramphenicol
  - 抗瘧／抗風濕藥：Chloroquine、Hydroxychloroquine
  - 他汀類：Rosuvastatin、Simvastatin
  - 放射性碘：Iodide I-131、Iodide I-123
  - 其他：Disulfiram、Dapsone、Zafirlukast、Adalimumab
  - 抗腫瘤藥：Paclitaxel、Cabazitaxel、Bortezomib、Brentuximab vedotin、Trastuzumab emtansine
- **類別風險提醒**：8-hydroxyquinoline 類藥物有神經毒性疑慮（如亞急性脊髓視神經病變），長期使用需特別審慎。這與上述周邊神經與視神經相關禁忌相呼應。

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 骨放射壞死的預測僅來自模型分數，沒有臨床試驗、文獻或機轉資料支持（L5）。
- 藥物的神經毒性風險，加上原廠仿單的警語與禁忌資料尚未取得，現階段不適合推進。

**若要推進需要：**
- 取得 Diiodohydroxyquinoline 的作用機轉資料（DrugBank）
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性篩選
- 進行針對骨放射壞死的文獻回顧，確認是否有前臨床或機轉研究
- 評估給藥途徑：香港現有製劑為陰道錠，與骨放射壞死所需的給藥途徑可能不相容
- 若有前臨床證據，再評估長期使用的神經毒性風險與替代的預測適應症（例如肺炎方向的文獻需閱讀全文確認相關性）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

