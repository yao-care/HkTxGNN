---
layout: default
title: Chlordiazepoxide
parent: 中證據等級 (L3-L4)
nav_order: 183
evidence_level: L4
indication_count: 10
---

# Chlordiazepoxide
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Chlordiazepoxide：從焦慮症到失眠

## 一句話總結

Chlordiazepoxide（利眠寧）是最早問世的苯二氮平類（benzodiazepine）藥物，文獻中主要作為抗焦慮藥使用。
TxGNN 模型預測它可能對**失眠 (Insomnia)** 有效，但目前**沒有直接相關的臨床試驗**。
支持的文獻只有間接證據，多為綜述、藥動學和老年用藥風險研究，沒有針對此藥與失眠的 RCT。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明；依文獻為焦慮症相關用途 |
| 預測新適應症 | 失眠 (Insomnia) |
| TxGNN 預測分數 | 99.998% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Chlordiazepoxide 是 GABA-A 受體的正向異位調節劑（positive allosteric modulator）。這一類藥物有公認的鎮靜安眠作用，可縮短入睡時間、減少夜間醒來次數。DrugBank 的作用機轉欄位目前沒有資料，以上機轉推論來自模型的理由說明。

從抗焦慮到助眠，兩者都靠增強 GABA 的抑制性訊號傳遞，因此機轉上說得通。另有一個相近的預測項目「入睡與維持睡眠障礙 (Sleep disorder, initiating and maintaining sleep)」，分數為 99.877%，與失眠高度重疊，建議合併評估。

但要留意：這個藥的活性代謝物半衰期長，隔天嗜睡、跌倒和依賴的風險都要納入考量，長者尤其明顯。現有文獻沒有一篇是 chlordiazepoxide 治療失眠的 RCT，所以合理性目前只停留在機轉層次。

## 臨床試驗證據

目前無相關臨床試驗登記。

資料中雖有一筆比對結果（NCT01109030），但內容是 pioglitazone 用於憂鬱症，與本藥和失眠皆無關，屬於誤配，已排除。

## 文獻證據

以下依失眠與睡眠障礙兩個預測項目彙整。臨床試驗類優先，其餘依相關性排列。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3536890](https://pubmed.ncbi.nlm.nih.gov/3536890/) | 1986 | 隨機雙盲試驗（複方） | J Clin Psychiatry | Limbitrol（chlordiazepoxide＋amitriptyline）比單用 amitriptyline 更快改善症狀；兩組睡眠實驗室指標無差異 |
| [6137426](https://pubmed.ncbi.nlm.nih.gov/6137426/) | 1983 | 隨機雙盲試驗（間接） | J Int Med Res | 酒精戒斷治療中，clobazam 與 chlordiazepoxide 都有效，焦慮量表上 clobazam 較佳；與失眠無直接關係 |
| [7595266](https://pubmed.ncbi.nlm.nih.gov/7595266/) | 1995 | Review | J Fam Pract | 回顧社區長者使用苯二氮平治療失眠的效益與風險；缺乏長期療效研究 |
| [2883822](https://pubmed.ncbi.nlm.nih.gov/2883822/) | 1986 | Review | Acta Psychiatr Scand Suppl | 長者對苯二氮平的反應增強，且無法單以血中濃度差異解釋 |
| [4365779](https://pubmed.ncbi.nlm.nih.gov/4365779/) | 1974 | 比較研究 | Br J Psychiatry | 依標題為 chlordiazepoxide 與 amylobarbitone 的安眠效果比較（無摘要） |
| [22521806](https://pubmed.ncbi.nlm.nih.gov/22521806/) | 2013 | Review | Eur Psychiatry | 重新評估苯二氮平在精神科的角色；安全性優於巴比妥類 |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | 抗焦慮藥的藥物動力學回顧 |
| [30680986](https://pubmed.ncbi.nlm.nih.gov/30680986/) | 2019 | 橫斷面研究 | Med Glas | 依 Beers 準則評估伊朗長者的潛在不適當用藥 |
| [559235](https://pubmed.ncbi.nlm.nih.gov/559235/) | 1977 | 用藥評論 | Med Lett Drugs Ther | 選擇苯二氮平治療焦慮或失眠的建議（無摘要） |
| [6111745](https://pubmed.ncbi.nlm.nih.gov/6111745/) | 1981 | 用藥評論 | Med Lett Drugs Ther | 苯二氮平的選擇（無摘要） |

## 其他預測適應症概況

其餘預測項目證據薄弱，目前皆建議暫緩。

| 預測適應症 | 分數 | 證據等級 | 評估 |
|-----------|------|---------|------|
| 馬尾症候群 | 99.996% | L5 | 無試驗或文獻；苯二氮平無法處理壓迫性病因 |
| 神經性膀胱（已淘汰術語） | 99.975% | L5 | 無直接機轉連結，疾病術語已淘汰 |
| 注意力不足過動症（注意力不集中型） | 99.956% | L5 | 苯二氮平可能損害注意力，方向可能不利 |
| 特定發展障礙 | 99.929% | L4 | 僅有 1975 年自閉症藥物治療綜述，以及產前暴露造成空間學習缺損的動物研究，後者是傷害訊號 |
| 巴比妥類濫用 | 99.868% | L4 | 與巴比妥類有交叉耐受，但文獻多為酒精戒斷，屬間接證據；濫用風險需嚴控 |
| 迷幻藥濫用 | 99.868% | L4 | 僅能症狀性緩解焦慮或激動，文獻無直接證據 |
| 抗憂鬱藥類濫用 | 99.868% | L4 | 證據僅有舊文獻與小鼠篩檢；本藥自身有依賴性 |
| 肌筋膜疼痛症候群 | 99.790% | L4 | 僅有 1975 年非典型顏面痛病例分析，屬相關但不同的疾病 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-23045 | LITAMIN TAB 5MG | CHRISTO PHARM LTD |
| HK-11504 | CHLORDIAZEPOXIDE CAP 5MG | UNICORN LABORATORIES O/B AMERICAN UNICORN LABORATORIES LIMITED |
| HK-27469 | CHLORDIAZEPOXIDE CAP 2.5MG | UNICORN LABORATORIES O/B AMERICAN UNICORN LABORATORIES LIMITED |
| HK-35045 | MEDOCALUM TAB | STAR MEDICAL SUPPLIES LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

文獻與模型分析提示的風險，包括：

- 半衰期長的活性代謝物，可能造成隔天嗜睡、跌倒與認知功能受損，長者尤其需要注意。
- 有依賴性與濫用的潛在風險，以及停藥後的戒斷症候群。
- 動物研究顯示產前暴露可能造成學習缺損，孕婦使用需審慎。

## 結論與下一步

**決策：Hold**

**理由：**
- 模型分數很高，苯二氮平類的助眠作用機轉也合理，但沒有任何 chlordiazepoxide 治療失眠的直接臨床試驗，文獻只有綜述與間接證據。
- 香港仿單的警語與禁忌尚未取得（阻擋性資料缺口），無法進入安全性篩選；長半衰期加上依賴風險，也使它相較於已有較佳證據的安眠藥缺乏優勢。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語、禁忌症與原核准適應症。
- 補上 DrugBank 的作用機轉資料。
- 系統性檢索 chlordiazepoxide 對失眠的對照試驗，並與已核准的安眠藥比較療效與安全性。
- 將「失眠」與「入睡與維持睡眠障礙」合併為單一研究問題評估。
- 針對長者與依賴風險族群，設計使用限制與監測方案。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

