---
layout: default
title: Pegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 566
evidence_level: L5
indication_count: 2
---

# Pegfilgrastim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Pegfilgrastim：原適應症資料缺失 → 糖尿病視網膜病變（預測）

## 一句話總結

Pegfilgrastim（DB00019）目前在香港**未上市**，且本評估的原始適應症與作用機轉資料均缺失。
TxGNN 模型預測它可能對**重度非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)** 有效，
但目前**無任何臨床試驗、無任何文獻**支持，僅為模型預測（證據等級 L5）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（本評估未取得授權適應症紀錄） |
| 預測新適應症 | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L5（僅模型預測，無臨床試驗或文獻） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（original_moa 為資料缺口）。根據 TxGNN 分析文字，Pegfilgrastim 是長效型 G-CSF（顆粒球群落刺激因子）類似物，機轉上會刺激骨髓顆粒球前驅細胞增殖分化，並動員 CD34+ 幹細胞／內皮前驅細胞（EPC）進入周邊血液。模型的高分可能反映知識圖譜中「G-CSF 促進 EPC 動員」與「視網膜血管修復」路徑的間接連結。

但這個機轉存在明確的**方向性風險**：G-CSF 動員 EPC 所伴隨的促血管新生（pro-angiogenic）性質，在已有異常視網膜血管反應的糖尿病視網膜病變患者身上，理論上可能加速病變惡化，而非產生保護效果。文獻上曾有 G-CSF/GM-CSF 使用後視網膜出血或病變惡化的個案報告。目前沒有任何直接臨床證據能確認此關聯的方向是保護或有害，機轉連結純屬推測。

第二個預測適應症（一般性糖尿病視網膜病變，score 99.73%）同樣基於相同機轉假設，同樣無臨床試驗或文獻佐證，風險考量與上述一致。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Pegfilgrastim 目前未在香港上市，無許可證登記資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

（註：TFDA 仿單警語與禁忌症目前為 Blocking 等級資料缺口，尚無法進行安全性初評。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 兩項預測適應症皆為 L5（僅模型預測，無臨床試驗或文獻佐證），且機轉關聯的作用方向不明確，甚至可能與治療目的相反（促血管新生 vs. 視網膜病變惡化風險）。
- 原廠作用機轉（MOA）與 TFDA 仿單警語/禁忌等關鍵安全性資料均缺失，尚不足以支持任何臨床行動。

**若要推進需要：**
- 補齊 TFDA 仿單警語與禁忌症（DG001，Blocking 等級）
- 補齊作用機轉資料以釐清機轉關聯性（DG002）
- 針對「G-CSF/EPC 動員對糖尿病視網膜病變是保護還是惡化」進行機轉方向性的臨床前研究或藥物安全通報（pharmacovigilance）查證
- 若機轉方向確認為風險而非保護，應考慮將此候選降級或排除
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

