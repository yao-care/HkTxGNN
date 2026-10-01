---
layout: default
title: Econazole
parent: 僅模型預測 (L5)
nav_order: 301
evidence_level: L5
indication_count: 7
---

# Econazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Econazole：從局部抗黴菌治療到 Majocchi 肉芽腫

## 一句話總結

Econazole 是咪唑類（imidazole）抗黴菌藥，在香港以陰道栓劑、外用溶液和乳膏等劑型上市。
TxGNN 模型預測它可能對 **Majocchi 肉芽腫 (Majocchi granuloma)** 有效，但目前**沒有臨床試驗**，只有 **1 篇病例報告**，且該報告並未評估 econazole 的療效。因此這項預測只有模型分數支持，實際證據很薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症（依藥物類別為局部抗黴菌治療） |
| 預測新適應症 | Majocchi 肉芽腫 (Majocchi granuloma) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L4（僅 1 篇非 econazole 專屬的病例報告，實質接近 L5） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 16 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Econazole 抑制真菌的羊毛固醇 14-α-去甲基酶（CYP51），使麥角固醇（ergosterol）耗竭，破壞真菌細胞膜。這個機轉對造成 Majocchi 肉芽腫的皮癬菌（如紅色毛癬菌 *Trichophyton rubrum*）理論上有效，這也是模型給出高分的主要原因。

不過，Majocchi 肉芽腫是毛囊及毛囊周圍的深層感染。外用唑類藥物一般滲透力不足，臨床上通常需要全身性抗黴菌治療。TxGNN 的高分（99.97%）很可能來自「皮癬菌－唑類藥物」在知識圖譜中的相鄰關係，並不代表 econazole 外用製劑能有效治療深層病灶。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37899944](https://pubmed.ncbi.nlm.nih.gov/37899944/) | 2023 | 病例報告 | Case Reports in Dermatology | 以一位 54 歲男性為例，說明黴菌感染常被誤認為濕疹或乾癬，誤用外用類固醇或鈣調神經磷酸酶抑制劑會造成 tinea incognita，使診斷更困難。該文未評估 econazole 的療效。 |

## 香港上市資訊

共 16 張許可證，以下列出 5 張。許可證資料未載明劑型與核准適應症，劑型為依品名推斷。

| 許可證號 | 品名 | 劑型（依品名） | 廠商 |
|---------|------|------|------|
| HK-36295 | ECOMI VAGINAL PESSARIES 150MG | 陰道栓劑 | CNW (HK) LTD |
| HK-34621 | ECONAZOLE SUPP 150MG "YUNG SHIN" | 栓劑 | YUNG SHIN CO LTD |
| HK-57772 | ZYME SOLUTION 10MG/ML | 溶液 | HITPHARM PHARMACEUTICAL CO LTD |
| HK-58828 | EKONA VAGINAL SUPP 150MG | 陰道栓劑 | WINGS PHARMACEUTICAL LTD |
| HK-54354 | PICOSONE CREAM | 乳膏 | WELLDONE PHARMACEUTICALS LIMITED |

## 其他預測適應症（供參考）

TxGNN 對 econazole 還預測了下列適應症。其中**外陰陰道念珠菌症**的證據明顯強於 Majocchi 肉芽腫，值得優先評估。

| 排名 | 預測適應症 | 分數 | 證據等級 | 建議 | 說明 |
|------|-----------|------|---------|------|------|
| 2 | Ectothrix 感染 | 99.97% | L5 | Hold | 毛髮外側侵犯型皮癬菌感染，無試驗或文獻，僅有圖譜關聯 |
| 3 | Endothrix 感染 | 99.97% | L5 | Hold | 毛髮內部侵犯，外用唑類難以到達，無臨床證據 |
| 4 | 表淺黴菌症 | 99.97% | L3 | Research Question | 屬類別層級的既有用藥，近乎標示確認而非真正再利用。econazole 專屬證據僅有 2026 年 1 篇耳黴菌症 MIC 與臨床反應相關性研究 |
| 5 | 頭皮或鬍鬚皮癬菌病 | 99.97% | L5 | Hold | 檢索到的文獻是關鍵字誤配（beard、scalp），與抗黴菌無關 |
| 6 | 深部皮癬 (Tinea profunda) | 99.96% | L5 | Hold | 外用 econazole 的深層組織滲透存疑，無臨床證據 |
| 7 | 外陰陰道念珠菌症 | 99.50% | L2 | Proceed with Guardrails | 見下方說明 |

**外陰陰道念珠菌症的證據摘要：**
- 有多項 econazole 專屬臨床研究：
  - 與 clotrimazole 的雙盲比較（1994，[PMID 7820892](https://pubmed.ncbi.nlm.nih.gov/7820892/)）。
  - 與 clotrimazole 的隨機比較（1980，178 名女性，[PMID 7383476](https://pubmed.ncbi.nlm.nih.gov/7383476/)），黴菌學治癒率相當。
  - 與 butoconazole 的隨機比較（1990，[PMID 2257961](https://pubmed.ncbi.nlm.nih.gov/2257961/)）。
  - 996 例多中心 3 日療程研究（1976，150 mg 陰道栓劑，治癒率 93.4%，[PMID 984105](https://pubmed.ncbi.nlm.nih.gov/984105/)）。
- 這些研究多為登錄制度建立前的文獻，未標示試驗階段。若確認為足夠檢定力的隨機對照試驗，證據等級可升為 L1。
- 唯一登記的臨床試驗 NCT00915629 是益生菌預防復發研究，並未測試 econazole。
- 香港已有 econazole 陰道栓劑上市（如 HK-36295、HK-58828），主要工作是核對本地標示，而非真正的再利用。
- 需留意對唑類抗藥的非白色念珠菌，以及生物膜相關的抗藥性（[PMID 37601561](https://pubmed.ncbi.nlm.nih.gov/37601561/)、[PMID 25442913](https://pubmed.ncbi.nlm.nih.gov/25442913/)）。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- Majocchi 肉芽腫這項預測沒有臨床試驗，唯一的文獻是與 econazole 療效無關的病例報告。
- 外用唑類對深層毛囊感染的滲透有限，臨床上通常需要全身性治療，因此不建議以外用 econazole 推進此適應症。

**若要推進需要：**
- 取得 econazole 對深層或毛囊性皮癬菌感染的組織滲透與臨床療效資料。
- 從香港衛生署下載並解析各許可證的仿單，確認核准適應症、警語與禁忌症（目前缺少，這是進入安全性篩選的阻礙）。
- 補充 econazole 的作用機轉（MOA）資料。
- 若要優先推進，建議先評估「外陰陰道念珠菌症」：確認舊有研究的設計與檢定力，並核對香港各許可證是否已標示此適應症。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

