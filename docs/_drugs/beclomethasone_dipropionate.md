---
layout: default
title: Beclomethasone Dipropionate
parent: 中證據等級 (L3-L4)
nav_order: 95
evidence_level: L3
indication_count: 1
---

# Beclomethasone Dipropionate
{: .fs-9 }

證據等級: **L3** | 預測適應症: **1** 個
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

# Beclomethasone Dipropionate：從（原適應症資料缺漏）到異位性皮膚炎

## 一句話總結

Beclomethasone Dipropionate 是一種糖皮質素（corticosteroid），在香港以吸入劑及鼻噴劑形式上市，但本資料未載明原適應症。
TxGNN 模型預測它可能對**異位性皮膚炎 (Atopic Eczema)** 有效，
目前**無臨床試驗登記**，有 **18 篇文獻**（其中僅 1 篇為 RCT，且為 1984 年的小型交叉試驗）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 異位性皮膚炎 (Atopic Eczema) |
| TxGNN 預測分數 | 99.41% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（列為研究問題） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Beclomethasone dipropionate 是糖皮質素受體促效劑，為前驅藥，在體內轉換為活性的 17-單丙酸酯。其廣泛的抗發炎與免疫抑制作用，理論上可抑制異位性皮膚炎中以第二型輔助 T 細胞（Th2）為主的皮膚發炎。

不過要注意，糖皮質素類藥物本來就是異位性皮膚炎的既有治療選項。0.994 的高分可能反映的是「類別層級」的既有知識，而非這個藥物特有的新發現。因此這個預測較像是既有用藥的延伸，而非真正的新穎再利用訊號。

此外，文獻中研究的給藥途徑差異很大（口服、鼻用、外用、密封敷料、微胞製劑），彼此無法直接比較，也不能直接對應到香港目前上市的吸入劑與鼻噴劑。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下依 RCT > 臨床研究 > 回顧 > 其他的順序列出，最多 10 篇。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [6434024](https://pubmed.ncbi.nlm.nih.gov/6434024/) | 1984 | RCT | Br Med J (Clin Res Ed) | 26 名重度異位性皮膚炎兒童，雙盲安慰劑對照交叉試驗；口服加鼻用 beclomethasone 治療 4 週後改善顯著優於安慰劑，未見不良反應，但 24 小時尿皮質醇略降 |
| [1476023](https://pubmed.ncbi.nlm.nih.gov/1476023/) | 1992 | 臨床研究 | Acta Derm Venereol Suppl | 口服 BDP 治療難治性兒童異位性皮膚炎，14 人中 10 人病情穩定控制；但在維持劑量下觀察到線性生長減緩的跡象 |
| [14522624](https://pubmed.ncbi.nlm.nih.gov/14522624/) | 2003 | 臨床研究 | J Dermatolog Treat | 8 名學齡前兒童使用類固醇濕敷療法，評估短期生長與骨代謝（安全性導向） |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | 回顧 | Neuroimmunomodulation | 鼻用類固醇與腎上腺抑制的關聯（安全性背景，非針對皮膚炎療效） |
| [30911861](https://pubmed.ncbi.nlm.nih.gov/30911861/) | 2019 | 前臨床 | AAPS PharmSciTech | BDP 混合微胞水凝膠於亞慢性皮膚炎動物模型的配方開發，無臨床療效資料 |
| [37023229](https://pubmed.ncbi.nlm.nih.gov/37023229/) | 2023 | 計算方法 | J Chem Inf Model | DrugRep-KG 知識圖譜藥物再利用方法論文，僅為預測 |
| [11488426](https://pubmed.ncbi.nlm.nih.gov/11488426/) | 2001 | 回顧 | Jpn J Pharmacol | 過敏性疾病用藥回顧，指出糖皮質素為最有效藥物（間接證據） |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | 回顧 | Allergy | 氣喘患者的糖皮質素過敏（間接證據） |
| [19874229](https://pubmed.ncbi.nlm.nih.gov/19874229/) | 2009 | 動物研究 | Immunopharmacol Immunotoxicol | 小鼠實驗比較 mometasone furoate 與 BDP 的局部抗發炎及全身效應，mometasone 局部效力較強、口服全身效應較低 |
| [9463794](https://pubmed.ncbi.nlm.nih.gov/9463794/) | 1998 | 回顧 | Drugs | 外用 mometasone 的藥理與治療回顧，其對異位性皮膚炎的效果與同效價糖皮質素相近（以 beclomethasone 類似物為主，非 BDP 本身） |

**證據限制：**
- 唯一的 RCT 樣本僅 26 人，且為 40 年前的口服加鼻用組合，不代表現行劑型。
- 多篇文獻聚焦安全性（腎上腺抑制、生長遲緩），提示全身給藥於兒童有風險。
- 其餘文獻多為間接證據，或與 BDP 用於異位性皮膚炎關聯薄弱。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63314 | BECLOMETASONE PRESSURISED INHALATION BP 200MCG/ACTUATION (CFC FREE) | 吸入劑（由品名判斷） | 資料未載明 |
| HK-58338 | BELAX AQUA NASAL SPRAY 42MCG/DOSE | 鼻噴劑（由品名判斷） | 資料未載明 |
| HK-60130 | BECLOMETASONE PRESSURISED INHALATION BP 250MCG | 吸入劑（由品名判斷） | 資料未載明 |
| HK-28384 | BECONASE AQUEOUS NASAL SPRAY 0.05% | 鼻噴劑（由品名判斷） | 資料未載明 |
| HK-61115 | BECLO-RINO AQUEOUS NASAL SPRAY 50MCG/DOSE | 鼻噴劑（由品名判斷） | 資料未載明 |

以上為 20 張許可證中的 5 張。目前香港上市劑型皆為吸入或鼻用，資料中未見外用劑型，這與異位性皮膚炎所需的給藥途徑不一致。

---

## 安全性考量

安全性資訊請參考原廠仿單。

補充說明：藥物交互作用查詢無結果。文獻中提示，全身性或大範圍使用 beclomethasone 可能造成腎上腺（HPA 軸）抑制，兒童並可能出現生長減緩（見 PMID 1476023、6434024、19571596）。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 糖皮質素類治療異位性皮膚炎的機轉合理，但高預測分數可能主要來自類別知識，而非 BDP 特有的新訊號。
- 直接證據僅有一項 1984 年的小型 RCT，無臨床試驗登記；香港現有劑型（吸入、鼻用）也無法直接對應皮膚適應症。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症（目前為阻擋性資料缺口）。
- 補充 DrugBank 的作用機轉資料。
- 釐清與既有外用糖皮質素相比的差異化價值（療效、安全性或劑型優勢）。
- 評估是否需要外用劑型，以及兒童使用的生長與 HPA 軸風險。
- 進行更新的文獻檢索，尋找現代對照試驗。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

