---
layout: default
title: Avapritinib
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

# Avapritinib：從 KIT/PDGFRA 激酶抑制（GIST/肥大細胞增多症）到 軸向脊柱幹骺端發育不良

## 一句話總結

Avapritinib 是一種口服小分子激酶抑制劑，已知以 KIT 和 PDGFRA 激酶為主要靶點，原適用於 PDGFRA 突變型胃腸道間質瘤（GIST）及系統性肥大細胞增多症（本次 Evidence Pack 中原適應症欄位缺失，依機轉脈絡推斷）。
TxGNN 模型預測其最高排名的潛在新適應症為**軸向脊柱幹骺端發育不良（Axial Spondylometaphyseal Dysplasia）**，預測分數達 99.92%。
然而，所有前十名預測均**無任何臨床試驗或文獻支持（L5 等級）**，且排名第一的機轉合理性低，評估單位在報告中明確指出此高分可能源於圖譜拓撲人工製品。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（依機轉推斷：GIST / 系統性肥大細胞增多症） |
| 預測新適應症（第一名） | 軸向脊柱幹骺端發育不良（Axial Spondylometaphyseal Dysplasia） |
| TxGNN 預測分數 | 99.92%（Rank #2089） |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | ✗ 未上市（0 張許可證） |
| 許可證數 | 0 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

### 藥物作用機轉

目前 Evidence Pack 中 Avapritinib 的詳細 MOA 欄位為資料缺口（[Data Gap]）。根據 `repurposing_rationale` 中反覆出現的 **KIT/PDGFRA 激酶抑制** 脈絡，可推斷 Avapritinib 的作用機轉在於選擇性抑制 KIT（尤其是 D816V 突變型）及 PDGFRA（尤其是 D842V 突變型）的活化，從而阻斷下游訊號傳遞（PI3K/AKT、RAS/MAPK 路徑），抑制腫瘤細胞增殖與存活，並對肥大細胞活化具有抑制效果。

### 原適應症與新適應症的關聯性評估

軸向脊柱幹骺端發育不良（Axial Spondylometaphyseal Dysplasia）為一種以 **BMPER 基因突變**為主要致病原因的罕見骨骼遺傳疾病，其核心機轉涉及骨型態發生蛋白（BMP）訊號路徑的異常。

然而，BMP 路徑與 KIT/PDGFRA 激酶路徑在目前已知的文獻中**無明確直接交集**。此預測在機轉合理性上相當薄弱，Evidence Pack 中的機轉分析也明確指出：「TxGNN 高分可能源於圖譜拓撲人工製品（graph topology artifact）」。

### 補充說明：ALS 相關預測（第 3、5、6 名）的潛在價值

值得注意的是，前十名中有三筆肌萎縮性側索硬化症（ALS）相關預測（Rank 3、5、6），其推薦決策為「Research Question」而非「Hold」。機轉假說為：ALS 患者脊髓組織中已觀察到肥大細胞浸潤，而肥大細胞高度表達 KIT/D816V；Avapritinib 抑制此靶點理論上可降低神經炎症。此為高度推測性的間接假說，但提供了一個可進行前臨床驗證的研究方向。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

（針對前十名預測適應症，共查詢 ClinicalTrials.gov 及 ICTRP，均無結果。）

---

## 文獻證據

目前無相關文獻。

（針對前十名預測適應症，共查詢 PubMed，均無結果。）

---

## 香港上市資訊

Avapritinib 目前在香港**未上市**，許可證數為 0，無相關許可證資料。

---

## 細胞毒性

Avapritinib 屬於抗腫瘤靶向藥物（KIT/PDGFRA 激酶抑制劑）。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 靶向藥物（Targeted Therapy）－小分子激酶抑制劑，非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 低至中度（相較傳統化療較低；已知不良事件包括貧血、中性球減少症） |
| 致吐性分級 | 低度（口服靶向藥物，致吐性通常低於傳統化療）|
| 監測項目 | CBC（含分類）、肝功能（AST/ALT）、腎功能、認知/神經系統症狀（顱內出血為已知警語，需監測） |
| 處置防護 | 需依細胞毒性藥物處置規範操作；注意顱內出血風險（尤其高齡患者或抗凝血劑併用者） |

> 詳細毒性資料請參考原廠仿單的警語與注意事項（本 Evidence Pack 中 MOA 及 TFDA 仿單資料均缺失）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

（本 Evidence Pack 安全性欄位均為資料缺口，包括 TFDA 仿單警語、禁忌症及藥物交互作用，均無法從本次資料集評估。）

---

## 結論與下一步

**決策：Hold**

**理由：**
所有前十名預測適應症均屬 L5 等級（僅模型預測，無任何臨床試驗或文獻支持）；排名第一的「軸向脊柱幹骺端發育不良」其機轉合理性極低，且報告系統明確指出高分可能為圖譜拓撲人工製品，缺乏進一步推進的生物學依據。

**若要推進需要：**

1. **補充 Avapritinib 完整 MOA 資料**（DG002）：查詢 DrugBank API 或文獻，確認 KIT/PDGFRA 抑制路徑的完整下游效應。
2. **補充 TFDA/香港 HA 仿單警語與禁忌症**（DG001）：下載官方仿單 PDF 並解析安全性章節，以完成 S1 安全性初評。
3. **重新評估是否聚焦 ALS 假說**：ALS 相關預測（Rank 3、5、6）具有初步機轉假說（肥大細胞-KIT-神經炎症路徑），建議以「研究問題」框架先進行體外或動物模型的前臨床驗證，再決定是否升級為正式研究候選。
4. **香港市場准入評估**：Avapritinib 目前香港未上市，若有臨床開發意圖，需評估臨床試驗申請路徑或孤兒藥資格申請可行性。

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。所有老藥新用候選需經嚴格臨床驗證方可應用於患者。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

