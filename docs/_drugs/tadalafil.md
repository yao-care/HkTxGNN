---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 846
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Tadalafil：預測新適應症為Ambras 型先天性全身性多毛症 (Ambras type hypertrichosis universalis congenita)（證據等級 L5）。原適應症：良性前列腺增生、肺動脈高壓、勃起功能障礙、心因性性交疼痛、早發性射精"
monitor_inn: "TADALAFIL"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality"]
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Tadalafil：從勃起功能障礙與肺動脈高壓到 Ambras 型全身性多毛症

## 一句話總結

Tadalafil 是 PDE5 抑制劑，原本用於良性前列腺增生、肺動脈高壓、勃起功能障礙、心因性性交疼痛與早發性射精。
TxGNN 模型預測它可能對 **Ambras 型先天性全身性多毛症 (Ambras type hypertrichosis universalis congenita)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 良性前列腺增生、肺動脈高壓、勃起功能障礙、心因性性交疼痛、早發性射精 |
| 預測新適應症 | Ambras 型先天性全身性多毛症 (Ambras type hypertrichosis universalis congenita) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Tadalafil 屬於 PDE5 抑制劑，可提高 cGMP 並促進血管擴張，這是它在勃起功能障礙與肺動脈高壓中發揮療效的基礎。

然而，Ambras 症候群是一種先天性多毛症，由影響 TRPS1 調控的基因體重組所致。PDE5 抑制劑與這種遺傳機轉之間，看不出明確的關聯。此預測很可能是知識圖譜中共享的毛髮或血管相關節點所造成的假象，不能視為證據。

另一個值得注意的是：同樣具血管擴張作用的 minoxidil 會引起多毛。若血管擴張與 cGMP 訊號真的影響毛囊微環境，Tadalafil 的方向反而可能是誘發毛髮生長，而非治療多毛。作用方向不明，且沒有資料支持。

其他排名較前的預測（多毛症、牙齒/牙周畸形症候群、Dandy-Walker 畸形相關症候群、遺傳性毛幹異常）同樣只有模型分數，沒有臨床試驗或文獻，也缺乏合理的機轉連結。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 20 張有效單方許可證，以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-51229 | CIALIS TAB 20MG | ELI LILLY ASIA, INC. |
| HK-68929 | CIATUFF 10 TABLETS 10MG | AUROBINDO PHARMA LIMITED |
| HK-67105 | TADAFLY TABLETS 20MG | TEVA PHARMACEUTICAL HONG KONG LIMITED |
| HK-65022 | ERETAF-20 TABLETS 20MG | HOVID LIMITED |
| HK-68018 | HAPPILONG TABLETS 5MG | LSB (HK) LIMITED |

---

## 安全性考量

- **知識圖譜中的禁忌疾病**（來自 TxGNN 知識圖譜，非仿單內容），主要包括：
  - 心血管與腦血管：主動脈狹窄、低血壓、急性冠心症、心肌梗塞、中風、腦梗塞、肥厚性心肌症
  - 血液相關：凝血疾病、鐮刀型貧血、血紅素病變、漿細胞骨髓瘤、白血病
  - 陰莖相關：陰莖異常勃起 (priapism)、Peyronie 病
  - 其他：肝衰竭、癲癇、聽力損失
- **藥物交互作用**：共查詢到 100 筆，以下為部分中度交互作用：
  - Aprepitant
  - Dexamethasone
  - Clarithromycin
  - Cimetidine
  - Miconazole
  - Clotrimazole
  - 多種 SGLT2 抑制劑（Canagliflozin、Dapagliflozin、Empagliflozin、Ertugliflozin）

  Papaverine 為輕度交互作用。

詳細的警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。
- 機轉上缺乏合理連結，且作用方向可能相反（血管擴張可能誘發多毛）。

**若要推進需要：**
- 取得詳細的作用機轉資料，並建立 PDE5/cGMP 訊號與毛囊或 TRPS1 通路的生物學依據
- 前臨床研究（如毛囊模型）驗證作用方向
- 取得香港仿單的警語與禁忌資料，完成安全性篩選
- 在無獨立生物學支持前，不建議投入臨床開發
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

