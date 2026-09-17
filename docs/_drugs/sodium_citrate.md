---
layout: default
title: Sodium Citrate
parent: 僅模型預測 (L5)
nav_order: 693
evidence_level: L5
indication_count: 5
---

# Sodium Citrate
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

# Sodium Citrate（DB09154）：五個預測適應症之老藥新用初步評估

## 一句話總結

Sodium Citrate 目前**未在香港上市**（0 張許可證），且原始核准適應症與作用機轉（MOA）資料均缺失。TxGNN 模型針對此藥物產出 5 個高分預測適應症，但僅**胃部疾病 (Stomach Disease)** 有實質文獻支持——多篇體外研究顯示 sodium citrate 可抑制胃癌細胞醣解並誘導凋亡；其餘 4 個候選（乳頭狀結膜炎、鼻腔疾病、急性咽喉炎、胃切除後症候群）皆無任何臨床試驗或文獻佐證。

---

## 五個候選適應症總覽

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|-----------|-----------|---------|---------|------|
| 1 | Papillary Conjunctivitis（乳頭狀結膜炎） | 99.95% | L5 | S0 | Hold |
| 2 | Nasal Cavity Disease（鼻腔疾病） | 99.95% | L5 | S0 | Hold |
| 3 | Acute Laryngopharyngitis（急性咽喉炎） | 99.94% | L5 | S0 | Hold |
| 4 | **Stomach Disease（胃部疾病）** | 99.89% | **L4** | **S1** | **Research Question** |
| 5 | Postgastrectomy Syndrome（胃切除後症候群） | 99.79% | L5 | S0 | Hold |

> 排名 1、2、3、5 之候選經人工複核後，其臨床試驗與文獻皆非直接測試 sodium citrate（多為其他 citrate 化合物或無關介入），TxGNN 高分可能反映知識圖譜中的間接關聯或化合物混淆，需以模型再校正處理，本報告後續聚焦於證據等級最高的**胃部疾病**候選。

## 快速總覽（最佳證據候選：胃部疾病）

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（未提供原始核准適應症） |
| 預測新適應症 | 胃部疾病 (Stomach Disease) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L4（體外前臨床研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold（受阻於安全性資料缺口） |

---

## 為什麼這個預測合理？

目前缺乏 sodium citrate 詳細的作用機轉資料，且原始核准適應症亦未提供，無法直接比對兩者的臨床關聯性。

不過，體外研究提供了初步的機轉線索：Sodium citrate 具鹼化及螯合鈣離子特性，與 3-bromopyruvate 併用時，可透過抑制腫瘤細胞的醣解（glycolysis）路徑，於胃癌細胞株（MGC-803、SGC-7901）誘導粒線體調控之細胞凋亡，並在小鼠原位移植腫瘤模型中觀察到腫瘤生長抑制效果。這些研究一致由同一團隊發表，屬體外/動物層級的前臨床證據（tier 3, L4），尚無任何臨床試驗直接測試 sodium citrate 於胃部疾病之療效。

同時需留意安全性負面訊號：文獻中另有個案報告顯示含 citrate 之腸道準備製劑（sodium picosulfate/magnesium citrate，非同一鹽類）曾導致食道與胃黏膜急性損傷，提示 citrate 類化合物對胃腸黏膜可能存在刺激性風險，此點在後續評估中應一併考量。

其餘 4 個候選適應症（乳頭狀結膜炎、鼻腔疾病、急性咽喉炎、胃切除後症候群）目前無任何機轉線索、臨床試驗或文獻支持，判定為模型雜訊或知識圖譜間接關聯，暫不建議投入資源。

---

## 臨床試驗證據（胃部疾病候選）

檢索到的試驗雖與「胃部疾病」關鍵字相關，但經相關性分級後**皆非直接測試 sodium citrate**（多為其他 citrate 鹽類如 bismuth citrate、alverine citrate，或不相關的化療/胃腸促動劑試驗），故不構成本候選的直接佐證：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06470386](https://clinicaltrials.gov/study/NCT06470386) | Phase 2/3 | 未招募 | 178 | Alverine citrate（非 sodium citrate）治療肝硬化門脈高壓 |
| [NCT04209933](https://clinicaltrials.gov/study/NCT04209933) | Phase 4 | 完成 | 240 | Bismuth potassium citrate 用於 H. pylori 四合一療法比較 |
| [NCT03425747](https://clinicaltrials.gov/study/NCT03425747) | Phase 4 | 完成 | 26 | Calcium citrate vs calcium carbonate 治療慢性副甲狀腺低能症 |
| [NCT06696248](https://clinicaltrials.gov/study/NCT06696248) | Phase 2/3 | 未招募 | 30 | Alverine citrate 併用 carvedilol 治療門脈高壓 |

*（其餘試驗因與 sodium citrate 無直接關聯，不逐一列出。）*

## 文獻證據（胃部疾病候選）

以下為直接以 sodium citrate（文獻中簡稱 SCT）作為研究對象的體外研究：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27163639](https://pubmed.ncbi.nlm.nih.gov/27163639/) | 2016 | 體外研究 | Biochem Biophys Res Commun | 3-Bromopyruvate 併用 sodium citrate 抑制醣解，誘導胃癌細胞株 MGC-803 粒線體調控凋亡 |
| [26708213](https://pubmed.ncbi.nlm.nih.gov/26708213/) | 2016 | 體外＋動物模型 | Oncology Reports | Sodium citrate 抑制 survivin 表現，於原位移植胃癌腫瘤模型中抑制生長 |
| [29115645](https://pubmed.ncbi.nlm.nih.gov/29115645/) | 2018 | 體外＋影像研究 | Oncology Reports | 以 18F-FDG PET/CT 評估 3-BrPA 與 sodium citrate 之醣解標靶治療效果 |
| [25073632](https://pubmed.ncbi.nlm.nih.gov/25073632/) | 2014 | 個案報告 | J Gastroenterol Hepatol | Citrate 類腸道準備劑（非同一鹽類）誘發食道/胃黏膜急性損傷（安全性負面訊號） |

---

## 香港上市資訊

目前 Sodium Citrate（DB09154）**未在香港上市**，無許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 本評估存在**阻斷性資料缺口（Blocking Data Gap）**：尚未取得仿單警語/禁忌症資料，此項缺口直接影響是否可進入 S1 安全性初評，須優先補齊。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 存在阻斷性安全性資料缺口（無仿單警語/禁忌症資料），依規則無法進入 S1 安全性初評。
- 5 個候選中僅胃部疾病達到 L4/S1，其餘 4 個皆為 L5（模型分數高但無任何實證支持），整體證據強度不足以支持推進。
- 即使是證據最強的胃部疾病候選，也僅止於體外/動物前臨床層級，尚無任何臨床試驗直接驗證 sodium citrate 之效果，且已有安全性負面訊號（citrate 類製劑之黏膜損傷個案）需一併評估。

**若要推進需要：**
- 優先取得 TFDA/原廠仿單完整警語與禁忌症資料（Blocking gap）
- 補充 sodium citrate 之作用機轉（MOA）資料
- 釐清藥物原始核准適應症，以評估與候選適應症之機轉關聯性
- 若欲推進胃部疾病候選，需設計動物體內或早期臨床試驗，驗證體外醣解抑制效果並評估胃腸黏膜安全性
- 對其餘 4 個 L5 候選（乳頭狀結膜炎、鼻腔疾病、急性咽喉炎、胃切除後症候群），建議暫緩投入資源，待模型或知識圖譜校正後再評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

