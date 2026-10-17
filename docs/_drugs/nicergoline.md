---
layout: default
title: Nicergoline
parent: 僅模型預測 (L5)
nav_order: 618
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Nicergoline：預測新適應症為毛髮過多症 (Hypertrichosis)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "NICERGOLINE"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "benign prostatic hyperplasia (disease)"]
---

# Nicergoline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Nicergoline：從（原適應症資料缺漏）到毛髮過多症

## 一句話總結

Nicergoline 是一種麥角衍生物，具 α1 腎上腺素受體拮抗與血管擴張作用，在香港已有上市許可，但本報告所整理的資料中未載明原核准適應症。
TxGNN 模型預測它可能對**毛髮過多症 (Hypertrichosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 毛髮過多症 (Hypertrichosis) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。一般已知 Nicergoline 為麥角衍生的 α1 腎上腺素受體拮抗劑與血管擴張劑，但它與毛髮生長調控之間的路徑並不明確。

TxGNN 分數很高（99.57%），但這來自知識圖譜的鄰近關係推論，並非生物學證據。值得注意的是，部分血管擴張劑（例如 minoxidil）反而會**引起**毛髮過多，因此若兩者之間真有關聯，較可能是不良反應型的關聯，而非治療效果。

其他排名靠前的預測也缺乏支持：
- **Ambras 型先天性全身性毛髮過多症**（99.43%）：屬罕見先天性疾病，與 TRPS1 調控區域的基因體重排有關，Nicergoline 的作用機轉無法處理此成因，分數可能只是反映與一般毛髮過多症節點的圖譜鄰近性。
- **伴有牙齒／牙周成分的畸形症候群**（99.42%）與 **以 Dandy-Walker 畸形為主要特徵的症候群**（99.41%）：皆為結構性發育缺陷，沒有合理的機轉依據。
- **良性前列腺增生 (BPH)**（99.39%，證據等級 L4，標示為「研究問題」）：這是五項預測中生物學上最合理的一項。Nicergoline 的 α1 受體拮抗作用與 tamsulosin、alfuzosin、doxazosin 等已確立的 BPH 藥物同屬一類機轉。不過這僅是類別推論，其 α1 親和力與泌尿道選擇性相較於已核准藥物並無資料，且需考量姿勢性低血壓風險。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-33548 | SERMION TAB 30MG | 未載明 | 未載明 |
| HK-06209 | SERMION TAB 5MG | 未載明 | 未載明 |
| HK-19045 | SERMION TAB 10MG | 未載明 | 未載明 |

三張許可證皆為單一成分製劑，狀態有效，持有者為 VIATRIS HEALTHCARE HONG KONG LIMITED。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 毛髮過多症的預測僅來自模型，沒有任何臨床試驗或文獻佐證，機轉上也缺乏連結，甚至可能是不良反應型的關聯。
- 其餘四項預測同樣缺乏證據，其中只有 BPH 具備類別層級的藥理合理性。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認原適應症、警語與禁忌症。
- 補齊 DrugBank 的作用機轉資料。
- 針對 BPH 方向進行文獻檢索，並比較 Nicergoline 與已核准 α1 阻斷劑的受體結合特性與泌尿道選擇性，同時評估姿勢性低血壓風險。
- 毛髮過多症及其他三項預測在取得任何機轉或臨床證據前，不建議投入進一步資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

