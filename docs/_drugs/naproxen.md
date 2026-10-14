---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 608
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Naproxen：從關節炎與疼痛症狀到短指併指症候群

## 一句話總結

Naproxen 是一種非類固醇消炎止痛藥（NSAID），原本用於關節炎、痛風、肌腱炎、偏頭痛等疼痛與發炎性疾病。
TxGNN 模型預測它可能對**短指併指症候群 (Brachydactyly-Syndactyly Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型的計算預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 滑囊炎、類風濕性關節炎、僵直性脊椎炎、肌腱炎、痛風、偏頭痛、骨關節炎等（香港許可證未載明適應症文字，此處依知識圖譜資料） |
| 預測新適應症 | 短指併指症候群 (Brachydactyly-Syndactyly Syndrome) |
| TxGNN 預測分數 | 99.35% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。依一般藥理知識，Naproxen 是非選擇性 COX-1/COX-2 抑制劑，透過減少前列腺素合成來緩解發炎與疼痛。

短指併指症候群是先天性骨骼畸形，成因屬發育期的遺傳異常（常涉及 HOXD13 或 BMP/GDF5 等訊息路徑）。抗發炎作用並不能矯正結構性的發育缺陷，因此機轉上**難以支持**這項預測。

這個高分較可能來自知識圖譜中與骨骼、肌肉骨骼疾病註記的鄰近關係（Naproxen 的原適應症包含關節病變與骨關節炎），而非真正的藥理關聯。

其他排名靠前的預測（先天性骨骼或眼部畸形症候群、肢中部發育不良、短脊椎－牙釉質發育不全症候群）也有相同問題：都是遺傳性發育異常，且同樣沒有證據支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Naproxen 在香港有 20 張有效的單方許可證，以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43951 | SOREN TAB 275MG | 錠劑（依品名） | 未提供 |
| HK-65797 | NAPROXEN TABLETS 250MG | 錠劑（依品名） | 未提供 |
| HK-56618 | SYN-NAPROXEN TAB 250MG | 錠劑（依品名） | 未提供 |
| HK-68279 | SELADIN TABLETS 250MG | 錠劑（依品名） | 未提供 |
| HK-44905 | NAPXEN TAB 250MG | 錠劑（依品名） | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（來自知識圖譜的藥物－疾病關聯，非仿單內容）：高血壓、心臟衰竭、冠狀動脈疾病、心肌梗塞、中風與腦血管疾病、肝臟疾病與肝衰竭、腎臟疾病、血液凝固異常、貧血、糖尿病、癲癇、骨質疏鬆、肥胖、物質濫用／依賴等。
- **藥物交互作用**：共查得 100 筆，以下為資料中列出的中度交互作用（部分）：
  - 制酸／胃藥類：Famotidine、Ranitidine、Cimetidine、Rabeprazole、Dexlansoprazole
  - 類固醇類：Hydrocortisone、Dexamethasone、Betamethasone、Budesonide、Triamcinolone
  - 其他 NSAID／水楊酸類：Acetylsalicylic acid、Mesalazine、Balsalazide
  - 降血糖藥：Metformin、Chlorpropamide
  - 其他：Aprepitant、Potassium citrate、Potassium bicarbonate、Picosulfuric acid、Polyethylene glycol (3350 with electrolytes)

仿單的警語與禁忌症資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型計算，沒有任何臨床試驗或文獻（證據等級 L5）。
- 短指併指症候群是發育性的遺傳畸形，Naproxen 的 COX 抑制與抗發炎作用在機轉上無法解釋其療效。

**若要推進需要：**
- 補齊 Naproxen 的作用機轉資料與香港仿單的警語、禁忌症資料。
- 以文獻與前臨床研究，確認 Naproxen 與 GDF5/BMP 或 HOXD13 相關路徑之間是否真有關聯。
- 如果仍要探索，需先確認這個疾病有哪些可治療的目標（例如繼發性疼痛的症狀處置），再另行評估。這類用途屬於症狀緩解，不是疾病修飾。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

