---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 846
evidence_level: L5
indication_count: 8
monitor_inn: "TADALAFIL"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
last_modified_at: 2026-10-23
description: "Tadalafil：預測新適應症為Ambras 型先天性全身多毛症（證據等級 L5）。原適應症：知識圖譜記錄的關聯：良性前列腺增生、肺動脈高壓、勃起功能障礙、心因性性交疼痛、早洩"
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## Tadalafil：從勃起功能障礙等泌尿與肺部適應症到安布拉斯型全身性先天多毛症
{: .text-alpha }

## 一句話總結

Tadalafil 是一種 PDE5 抑制劑，知識圖譜中記錄的原有用途包括勃起功能障礙、良性前列腺增生與肺動脈高壓。
TxGNN 模型預測它可能對 **Ambras 型先天性全身多毛症 (Ambras type hypertrichosis universalis congenita)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯：良性前列腺增生、肺動脈高壓、勃起功能障礙、心因性性交疼痛、早洩（香港許可證資料未提供適應症文字，無法以許可證確認） |
| 預測新適應症 | Ambras 型先天性全身多毛症 |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Tadalafil 屬於 PDE5 抑制劑，可提高細胞內 cGMP，作用於一氧化氮—cGMP 的血管舒張路徑。

Ambras 症候群是罕見的遺傳性毛髮發育異常，與染色體重組影響 TRPS1 調控有關。目前沒有已知的路徑能把 PDE5 抑制與此疾病連結。這個高分（0.9998）來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性（如與其他多毛症條目的相似性），而非生物學證據，也不代表 Tadalafil 特有的機轉。

整體而言，此預測應視為純計算結果，合理性有限。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

（補充：預測排名第 8 的「腦幹先兆偏頭痛」有一篇 2006 年個案報告 PMID [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/)，指出 Tadalafil 與典型偏頭痛先兆相關，方向為可能誘發而非治療，且與本報告主要預測的疾病無關。）

---

## 香港上市資訊

以下為已列出的前 5 張許可證（總數至少 20 張，清單可能不完整），均為單一成分製劑、狀態有效。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68929 | CIATUFF 10 TABLETS 10MG | 未提供 | 未提供 |
| HK-65022 | ERETAF-20 TABLETS 20MG | 未提供 | 未提供 |
| HK-68281 | TADALAFIL AZEVEDOS TABLETS 20MG | 未提供 | 未提供 |
| HK-66745 | DURACOR TABLETS 20MG | 未提供 | 未提供 |
| HK-66950 | FIP TADALAFIL TABLETS 20MG | 未提供 | 未提供 |

---

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：肝衰竭、癲癇、主動脈瓣狹窄、低血壓、凝血疾病、急性冠心症、鐮狀細胞貧血、中風與腦血管疾病、心肌梗塞、血紅素病變、多發性骨髓瘤、陰莖異常勃起、Peyronie 病、聽力損失、白血病、肥厚型心肌病變等。
- **藥物交互作用**（共查得 100 筆，以下為部分中度交互作用）：Aprepitant、Dexamethasone、Lorcaserin、Canagliflozin、Cimetidine、Clarithromycin、Dapagliflozin、Empagliflozin、Sapropterin、Miconazole、Clotrimazole、Ertugliflozin、Troglitazone。
- **其他訊號**：Tadalafil 與偏頭痛先兆的個案報告顯示可能有神經血管方面的不良反應。

仿單的主要警語與禁忌資料未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測疾病沒有任何臨床試驗或文獻支持，機轉上也缺乏合理連結，僅有模型分數。
- 其他預測中，「脊柱後側彎性心臟病」因肺高壓的間接關聯在生物學上相對合理，但同樣缺乏資料。多毛症方向甚至可能與血管擴張劑導致多毛的效果相反。

**若要推進需要：**
- 取得 Tadalafil 的作用機轉資料與香港仿單的警語、禁忌。
- 建立 PDE5/cGMP 與毛囊或 TRPS1 調控之間的機轉證據（體外或前臨床研究）。
- 系統性檢索該疾病的文獻與試驗，並確認作用方向（治療或誘發）。
- 若要探索替代方向，可優先評估與肺高壓相關的預測（如脊柱後側彎性心臟病），並評估缺氧性肺病中的通氣灌注風險。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

