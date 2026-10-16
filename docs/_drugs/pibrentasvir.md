---
layout: default
title: Pibrentasvir
parent: 僅模型預測 (L5)
nav_order: 696
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Pibrentasvir：預測新適應症為B 型肝炎病毒感染 (Hepatitis B virus infection)（證據等級 L5）。原適應症：慢性 C 型肝炎病毒感染 (chronic hepatitis C virus infection)"
monitor_inn: "PIBRENTASVIR"
predicted_indications: ["hepatitis B virus infection", "HIV infectious disease", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal"]
---

# Pibrentasvir
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

# Pibrentasvir：從慢性 C 型肝炎到 B 型肝炎病毒感染（模型預測）

## 一句話總結

Pibrentasvir 是 NS5A 抑制劑，與 glecaprevir 組成複方（Maviret），原本用於慢性 C 型肝炎治療。
TxGNN 模型預測它可能對 **B 型肝炎病毒感染 (Hepatitis B virus infection)** 有效，但目前**沒有任何以 B 型肝炎為對象的臨床試驗或文獻**，此預測僅有模型分數支持，機轉上並不合理。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 C 型肝炎病毒感染 (chronic hepatitis C virus infection) |
| 預測新適應症 | B 型肝炎病毒感染 (Hepatitis B virus infection) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 pibrentasvir 抑制 HCV 的 NS5A 蛋白，而 NS5A 是 HCV 特有的目標，HBV 並無對應的同源蛋白。

HBV 是 DNA 病毒（嗜肝 DNA 病毒科），透過前基因體 RNA 的反轉錄進行複製，與 HCV 的複製方式完全不同，因此直接的抗病毒機轉並不成立。TxGNN 的高分（99.84%）較可能反映的是知識圖譜中病毒性肝炎相關名詞之間的網路鄰近性，而非真正的藥理連結。

與 HBV 相關的唯一臨床意義是安全面：在 HBV/HCV 共感染患者使用 HCV 直接作用抗病毒藥物（DAA）時，需留意 HBV 再活化的風險。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

下列文獻皆以 HCV 為主題，並非 B 型肝炎療效證據。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Cohort | J Viral Hepat | 台灣 108 位重度腎功能不全的慢性 C 肝患者使用 GLE/PIB 的真實世界療效與安全性 |
| [32389183](https://pubmed.ncbi.nlm.nih.gov/32389183/) | 2020 | 臨床研究（Phase 3） | Lancet Gastroenterol Hepatol | DAA 併用 ezetimibe 短療程，預防接受 HCV 感染捐贈者器官的受贈者感染 HCV |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Review | Lancet Gastroenterol Hepatol | 兒童與青少年 C 肝的 DAA 治療概況 |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | 兒童病毒性肝炎處置；指出 HBV 治療目前仍遠未達根治 |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | DAA 治療失敗後的 C 肝再治療 |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | C 肝治療的藥動學與藥效學（2019 更新） |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | 病毒學實驗研究 | Hepatology | HCV 蛋白酶抑制劑抗藥突變株的演化路徑 |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | 會議報告 | AIDS Rev | 2017 國際病毒性肝炎會議報告 |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | 慢性 C 肝的診斷與治療簡介 |
| [42127258](https://pubmed.ncbi.nlm.nih.gov/42127258/) | 2026 | 會議報告 | Top Antivir Med | CROI 2026 病毒性肝炎進展，未涉及 pibrentasvir 對 HBV 的證據 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65653 | MAVIRET TABLETS | — | — |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測缺乏機轉依據（NS5A 為 HCV 特有目標，HBV 無同源蛋白），也沒有任何針對 B 型肝炎的臨床試驗或文獻，僅有模型分數支持，證據等級為 L5。
- 其他排名較前的預測（HIV、E 型肝炎、A 型肝炎等）同樣屬於名詞相似性或 HCV 試驗被誤對應的結果，沒有更好的替代方向。

**若要推進需要：**
- 取得詳細的作用機轉資料（MOA），並評估對 HBV 的任何潛在抗病毒活性。
- 進行體外 HBV 複製模型的抗病毒活性試驗，確認是否有任何實際效果。
- 取得香港原廠仿單的警語、禁忌與核准適應症資料，補足安全性評估。
- 在 HBV/HCV 共感染族群中，持續關注 HBV 再活化的安全性監測，這屬於現有適應症的用藥安全，而非新適應症的證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

