---
layout: default
title: Methylene Blue
parent: 僅模型預測 (L5)
nav_order: 490
evidence_level: L5
indication_count: 3
---

# Methylene Blue
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# METHYLENE BLUE：TxGNN 老藥新用評估（3 項預測適應症）

## 一句話總結

Methylene Blue 目前未在當地上市，無原適應症許可證資料，作用機轉（MOA）亦缺乏紀錄。TxGNN 模型針對此藥產出 3 個預測新適應症：**支氣管炎**、**高鐵血紅素血症**與**還原酶缺乏所致之高鐵血紅素血症**，合計有 **17 篇文獻**佐證、**無臨床試驗登記**。其中支氣管炎的預測經文獻覆核研判為知識圖譜共現假陽性，兩項高鐵血紅素血症預測則有明確且已臨床應用的機轉支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無公開許可證資料（本藥未於當地上市） |
| 藥物上市狀態 | 未上市（許可證數：0） |
| 預測新適應症 #1 | Bronchitis（支氣管炎）｜TxGNN 99.97%｜證據等級 L5｜建議 **Hold** |
| 預測新適應症 #2 | Methemoglobinemia, alpha type（高鐵血紅素血症）｜TxGNN 99.36%｜證據等級 L3｜建議 **Proceed with Guardrails** |
| 預測新適應症 #3 | Methemoglobinemia due to methemoglobin reductase deficiency（還原酶缺乏所致高鐵血紅素血症）｜TxGNN 99.36%｜證據等級 L4｜建議 **Research Question** |

## 為什麼這個預測合理？

目前缺乏 Methylene Blue 的詳細作用機轉（MOA）資料，也無原適應症紀錄可供比對，因此以下分析完全依據各預測適應症自身的機轉關聯性說明：

**支氣管炎**：文獻中 Methylene Blue 多作為支氣管鏡染色劑，用於區分良性與惡性支氣管病灶，屬於**診斷用途**而非治療用途；其餘文獻涉及精油氣管鬆弛、茶鹼感測器、抗憂鬱機轉等，與治療支氣管炎無直接關聯。高 TxGNN 分數應是知識圖譜中「methylene blue」與「bronchitis」高度共現（多為診斷情境）所致的假陽性。

**高鐵血紅素血症（兩型）**：Methylene Blue 經 NADPH 依賴之 methemoglobin reductase 途徑，被還原為 leukomethylene blue 後，可非酶促性地將 methemoglobin（Fe³⁺）還原為 hemoglobin（Fe²⁺），是治療後天性/藥物誘發性高鐵血紅素血症的經典機轉，且已為臨床標準用藥；對於先天性 cytochrome b5 reductase（diaphorase）缺乏所致的病例，Methylene Blue 提供繞過缺陷酵素的替代還原途徑，機轉合理，但目前證據以個案報告與犬隻病例系列為主。

## 各預測適應症詳細評估

### 1. Bronchitis（支氣管炎）— 建議 Hold

**機轉評估**：無實質治療機轉關聯，高分屬假陽性（見上）。

**臨床試驗證據**：目前無相關臨床試驗登記

**文獻證據**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9387672](https://pubmed.ncbi.nlm.nih.gov/9387672/) | 1996 | 診斷性描述 | 中華外科雜誌 | 47 例支氣管鏡染色，中央型肺癌染色率 97.14%，支氣管炎僅 8.33%，用於鑑別診斷而非治療 |
| [7313968](https://pubmed.ncbi.nlm.nih.gov/7313968/) | 1981 | 診斷性描述 | Terapevticheskii arkhiv | 以 methylene blue 進行染色內視鏡檢查，鑑別良惡性消化道及支氣管腫瘤 |
| [8420409](https://pubmed.ncbi.nlm.nih.gov/8420409/) | 1993 | 診斷/不相關 | Am Rev Respir Dis | 以 methylene blue 作為肺泡灌洗液稀釋指標，非治療用途 |
| [31419501](https://pubmed.ncbi.nlm.nih.gov/31419501/) | 2020 | 不相關藥理（精油） | J Ethnopharmacol | Lippia alnifolia 精油對氣管平滑肌鬆弛作用，與 methylene blue 無關 |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | 不相關分析化學 | Anal Chim Acta | 茶鹼電化學感測器開發，與 methylene blue 治療支氣管炎無關 |
| [21767626](https://pubmed.ncbi.nlm.nih.gov/21767626/) | 2011 | 不相關藥理 | J Ethnopharmacol | Aloysia gratissima 傳統用於支氣管炎等，與 methylene blue 無關 |
| [6121761](https://pubmed.ncbi.nlm.nih.gov/6121761/) | 1982 | 不相關藥物研究 | Int J Clin Pharmacol | β 受體阻斷劑研究，methylene blue 僅作為循環時間指示劑 |
| [20084922](https://pubmed.ncbi.nlm.nih.gov/20084922/) | 2009 | 不相關個案 | Mikrobiyoloji Bulteni | Moraxella catarrhalis 心內膜炎個案，與 methylene blue 無關 |
| [17120034](https://pubmed.ncbi.nlm.nih.gov/17120034/) | 2007 | 不相關個案 | Eur J Pediatr | 氣管食道瘻管個案，與 methylene blue 無關 |
| [2749902](https://pubmed.ncbi.nlm.nih.gov/2749902/) | 1989 | 基礎/不相關 | Tsitologiia | 紅血球高鐵血紅素細胞光譜學基礎研究 |

### 2. Methemoglobinemia, alpha type（高鐵血紅素血症）— 建議 Proceed with Guardrails

**機轉評估**：NADPH 依賴之 methemoglobin reductase 途徑還原 methemoglobin，為臨床標準解毒機轉。

**臨床試驗證據**：目前無相關臨床試驗登記

**文獻證據**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3537620](https://pubmed.ncbi.nlm.nih.gov/3537620/) | 1986 | Review | Medical Toxicology | 藥物/化學物誘發高鐵血紅素血症之臨床表現與處置，含 methylene blue 治療角色 |
| [26950891](https://pubmed.ncbi.nlm.nih.gov/26950891/) | 2016 | 基礎機轉研究 | J Photochem Photobiol B | Methylene blue 之光化學與生物活性研究，並提及溶血性貧血、高鐵血紅素血症等毒性 |

### 3. Methemoglobinemia due to methemoglobin reductase deficiency — 建議 Research Question

**機轉評估**：先天性 cytochrome b5 reductase 缺乏導致 methemoglobin 無法還原，Methylene Blue 提供替代性還原途徑，機轉合理但證據多為個案/動物病例。

**臨床試驗證據**：目前無相關臨床試驗登記

**文獻證據**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29845943](https://pubmed.ncbi.nlm.nih.gov/29845943/) | 2018 | 病例報告 | Neth J Med | 61 歲患者先天性高鐵血紅素血症，methylene blue 短暫改善後復發，確認 CYB5R3 基因變異 |
| [36638001](https://pubmed.ncbi.nlm.nih.gov/36638001/) | 2023 | 病例系列（犬） | Am J Vet Res | 犬隻 CYB5R 缺乏症長期口服 methylene blue 治療後之發炎表現型與 MetHb 變化 |
| [35202847](https://pubmed.ncbi.nlm.nih.gov/35202847/) | 2022 | 病例報告（犬） | Top Companion Anim Med | 犬隻 CYB5R 缺乏合併性發育異常，口服 methylene blue 治療 |
| [14109019](https://pubmed.ncbi.nlm.nih.gov/14109019/) | 1964 | 病例報告 | Arch Intern Med | 遺傳性 diaphorase 缺乏與高鐵血紅素血症 |
| [14248326](https://pubmed.ncbi.nlm.nih.gov/14248326/) | 1964 | 病例報告 | Arch Fr Pediatr | 隱性遺傳先天性高鐵血紅素血症合併 diaphorase I 缺乏之新病例 |

## 當地上市資訊

本藥目前**未於當地上市**，無許可證資料可供列出。

## 安全性考量

安全性資訊請參考原廠仿單。目前尚未取得當地仿單警語與禁忌症資料（列為 Blocking 級資料缺口），亦查無藥物交互作用資料。

## 結論與下一步

| 預測適應症 | 決策 |
|-----------|------|
| Bronchitis | **Hold** — 現有文獻多屬診斷用途或不相關，判定為假陽性，不建議投入資源 |
| Methemoglobinemia, alpha type | **Proceed with Guardrails** — 機轉明確且已為臨床標準用藥，可在安全性資料補齊後推進 |
| Methemoglobinemia due to reductase deficiency | **Research Question** — 機轉合理但僅有個案/動物證據，建議先規劃前瞻性病例收集或系統性回顧 |

**若要推進需要：**
- 取得當地仿單警語與禁忌症（目前為 Blocking 缺口，未解決前無法進入安全性初評）
- 補充 Methylene Blue 作用機轉（MOA）完整資料
- 確認本藥在當地的上市/引進路徑（目前為未上市狀態）
- 針對還原酶缺乏亞型，尋找人體系統性研究以提升證據等級
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

