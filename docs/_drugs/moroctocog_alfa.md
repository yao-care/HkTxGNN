---
layout: default
title: Moroctocog Alfa
parent: 中證據等級 (L3-L4)
nav_order: 508
evidence_level: L4
indication_count: 5
---

# Moroctocog Alfa
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# MOROCTOCOG ALFA：從 血友病A（Factor VIII 缺乏）到 血小板原發性釋放障礙

## 一句話總結

Moroctocog Alfa 是一種基因重組 Factor VIII（B 結構域缺失型），根據證據內文推斷原用於**先天性血友病 A** 的凝血因子替代治療（官方仿單資料尚缺）。
TxGNN 模型預測它可能對**血小板原發性釋放障礙 (Primary Release Disorder of Platelets)** 有效，但目前 **7 個臨床試驗**經逐一檢視後皆與此適應症無直接關聯，**無相關文獻支持**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 先天性血友病 A（依證據內文之機轉描述推斷；官方適應症/MOA 資料缺失，見 DG002） |
| 預測新適應症 | 血小板原發性釋放障礙 (Primary Release Disorder of Platelets) |
| TxGNN 預測分數 | 99.97%（KG 排名第 1073） |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Moroctocog Alfa 的詳細作用機轉資料（DG002，High severity）。根據證據內文的機轉分析，此藥為重組 Factor VIII，其藥理作用是補充凝血因子濃度以矯正**凝血因子缺乏**，原適應症應與先天性血友病 A 相關。

然而，血小板原發性釋放障礙（如 dense granule/alpha granule 缺陷）屬於**血小板顆粒釋放功能障礙**，病理機轉是血小板本身的分泌功能異常，並非凝血因子濃度不足。兩者致病機轉本質不同，FVIII 補充理論上**無法矯正**血小板釋放缺陷。

證據內文的機轉分析結論認為，TxGNN 給出的高分很可能源自知識圖譜中「出血傾向」節點的共現關係，而非真實藥理路徑——7 個檢索到的臨床試驗經逐一比對，皆與此病無直接關聯（COVID-19 疫苗後遺症、AML 凝血概況、肝衰竭人工肝支持、血友病 A 的 rFVIII Phase 3 試驗等），屬於雜訊而非實證。

> 補充說明：本證據包中排名第 4 的候選適應症「後天性凝血因子缺乏症 (acquired coagulation factor deficiency)」（含 13 個試驗、4 篇文獻，如 OBIZUR 相關研究）在機轉上與 FVIII 替代療法更為一致，可能是後續評估的優先方向，惟該候選之評分與建議仍標示為 pending。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | 招募中 | 200 | COVID-19 疫苗後綜合症之實驗室評估；與血小板釋放障礙無直接關聯（相關性 C） |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | 尚未招募 | 80 | 急性骨髓性白血病病人之血液凝血概況研究；相關性待評估 |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | 已完成 | 30 | rFVIII（BAX855）於既有血友病 A 病人手術期療效與安全性；為血友病 A 而非血小板釋放障礙（相關性 C） |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | 招募中 | 25 | 人工肝支持系統對慢加急性肝衰竭病人凝血功能之影響；相關性待評估 |
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | 已完成 | 159 | BIVV001（rFVIIIFc-VWF-XTEN）於成人重度血友病 A 之療效／安全性／藥動學；推測仍屬血友病相關試驗（相關性 C） |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | 已完成 | 74 | BIVV001 於兒童重度血友病 A 之療效與安全性；相關性待評估 |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | 招募中 | 45 | 經頸靜脈肝內門體分流術病人之全身/門脈止血功能探討；相關性待評估 |

**綜合判斷：** 上述 7 個試驗中已完成相關性評估者，均判定為與「血小板原發性釋放障礙」無直接關聯（多屬血友病 A 之 FVIII 產品試驗或不相關的凝血研究）。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

目前 Moroctocog Alfa 未在香港取得藥物許可證（登記許可證數：0），無上市資訊可供列出。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 注意：香港藥物警語/禁忌資料缺失已被標記為 **Blocking** 等級缺口（DG001），在此資料補齊前無法進入安全性初評（S1）階段。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉分析顯示 FVIII 補充在藥理上無法矯正血小板顆粒釋放功能障礙，7 個檢索到的臨床試驗均與此適應症無直接關聯，且無任何文獻支持，證據等級僅 L4、決策階段停留在 S0。
- 安全性基礎資料（仿單警語、禁忌症、MOA）尚缺，且其中仿單警語缺口為 Blocking 等級，尚無法通過 S1 安全性初評。

**若要推進需要：**
- 補齊 DrugBank／原廠仿單之作用機轉資料（DG002）
- 取得完整藥物警語與禁忌症資料以解除 Blocking 缺口，方能進入 S1 安全性初評（DG001）
- 若欲另闢方向，建議優先評估排名第 4 之候選適應症「後天性凝血因子缺乏症」，其機轉與 FVIII 藥理較為一致，且已有 13 個臨床試驗、4 篇文獻可供分析
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

