---
layout: default
title: Rifabutin
parent: 僅模型預測 (L5)
nav_order: 755
evidence_level: L5
indication_count: 5
---

# Rifabutin
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

# Rifabutin：從分枝桿菌感染到 HIV 感染症（HIV 相關機會性感染）

## 一句話總結

Rifabutin（立復丁）是 rifamycin 類抗分枝桿菌藥物，臨床上用於結核病與非結核分枝桿菌感染。
TxGNN 模型預測它可能對 **HIV 感染症 (HIV infectious disease)** 有效，目前有 **39 個臨床試驗**和 **20 篇文獻**。
證據主要支持它用於 **HIV 患者的伴隨感染**，即預防與治療鳥分枝桿菌複合群（MAC）及 HIV/結核共感染。它沒有直接的抗病毒作用，不能解讀為治療 HIV 本身。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | HIV 感染症 (HIV infectious disease) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L1（有多個已完成的 Phase 3 隨機試驗，但限於 HIV 相關分枝桿菌感染） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Rifabutin 屬於 rifamycin 類，作用是抑制細菌的 DNA 依賴性 RNA 聚合酶。它對 HIV 病毒沒有直接活性。目前缺乏 DrugBank 的詳細作用機轉資料，以上說明來自藥物類別的已知知識。

HIV 患者免疫力低下，常併發 MAC 菌血症與結核病。Rifabutin 在這兩類感染中有長期臨床經驗。與 rifampicin 相比，它對 CYP3A4 的誘導作用較弱，因此更適合與蛋白酶抑制劑（如 lopinavir/ritonavir）併用。TxGNN 的高分很可能反映了這些既有的知識圖譜關聯，而不是對 HIV 病毒本身的療效。

因此，這個預測合理的範圍是 **HIV 相關分枝桿菌感染的預防與治療**。若要主張它對 HIV 本身有效，目前沒有證據。

## 臨床試驗證據

共 39 個試驗，以下列出最相關的 10 個。其中 Phase 3 試驗是主要的療效證據。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | 完成 | 720 | 比較 azithromycin 與 rifabutin（單用或併用）預防 HIV 患者播散性 MAC 感染，並比較每日與每週 fluconazole 預防深部黴菌感染 |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | 完成 | 1100 | 比較 clarithromycin、rifabutin 與兩者併用，預防 CD4 ≤ 100 的 HIV 患者發生 MAC 菌血症 |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | 完成 | 400 | 四種治療方案比較，用於 AIDS 患者播散性 MAC 感染（clarithromycin 併用 ethambutol 加 rifabutin 或 clofazimine） |
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | 完成 | 450 | 在 clarithromycin/ethambutol 基礎上，比較 rifabutin 兩種劑量與安慰劑治療 MAC 菌血症 |
| [NCT00002267](https://clinicaltrials.gov/study/NCT00002267) | 未標示階段 | 完成 | 750 | 雙盲安慰劑對照，評估 rifabutin 單用預防 AIDS 患者 MAC 菌血症及對存活的影響 |
| [NCT00023361](https://clinicaltrials.gov/study/NCT00023361) | 未標示階段 | 完成 | 215 | 以間歇性 rifabutin 方案治療 HIV 相關結核病，評估治療失敗與復發率 |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | 完成 | 47 | 越南 TB/HIV 共感染患者，rifabutin 併用抗病毒治療的藥動學 |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Phase 2 | 完成 | 48 | 南非 TB/HIV 共感染患者，rifabutin 併用抗病毒治療的藥動學 |
| [NCT01663168](https://clinicaltrials.gov/study/NCT01663168) | Phase 2 | 未知 | 140 | EARNEST 子研究，評估 lopinavir/ritonavir 二線治療下不同 rifabutin 劑量的毒性與藥動學 |
| [NCT03478033](https://clinicaltrials.gov/study/NCT03478033) | 未標示階段 | 未知 | 230 | 前瞻性世代研究，比較含 rifampicin 或 rifabutin 的標準治療用於 HIV 合併肺結核的療效與安全性 |

其餘試驗多為藥物交互作用的藥動學研究，涵蓋 nelfinavir、efavirenz、maraviroc、dolutegravir 等抗病毒藥。

## 文獻證據

共 20 篇，以下列出最相關的 10 篇。沒有直接針對 HIV 的 RCT 文獻，多為世代研究、藥動學研究與回顧。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | 世代/藥動學研究 | J Antimicrob Chemother | 評估使用 lopinavir/ritonavir 二線 ART 的 TB/HIV 共感染兒童之 rifabutin 藥動學與安全性。先前一項兒童研究曾因嚴重嗜中性白血球低下而提早終止 |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | 世代研究 | J Antimicrob Chemother | 評估 rifabutin 用於 lopinavir/ritonavir 治療中的 HIV/TB 共感染兒童之安全性與療效；先前研究中 6 名兒童有 2 名出現需停藥的嗜中性白血球低下 |
| [25281400](https://pubmed.ncbi.nlm.nih.gov/25281400/) | 2015 | 藥動學/安全性研究 | J Antimicrob Chemother | 評估 rifabutin 與 lopinavir/ritonavir 併用於幼兒的短期安全性與藥動學 |
| [32979587](https://pubmed.ncbi.nlm.nih.gov/32979587/) | 2020 | 回溯觀察性研究 | Int J Infect Dis | 探討 tenofovir alafenamide 與 rifabutin 併用時抗病毒療效是否受影響；標題結論為併用不會導致 HIV-1 抑制失敗 |
| [26832753](https://pubmed.ncbi.nlm.nih.gov/26832753/) | 2016 | 族群藥動學彙整分析 | J Antimicrob Chemother | 整合既有資料描述 rifabutin 與 HIV 蛋白酶抑制劑的交互作用，並預測可達治療暴露量的劑量 |
| [9459473](https://pubmed.ncbi.nlm.nih.gov/9459473/) | 1998 | 觀察性研究 | JAMA | HIV 門診研究顯示 clarithromycin 與 rifabutin 可能對隱孢子蟲感染有化學預防效果 |
| [9093233](https://pubmed.ncbi.nlm.nih.gov/9093233/) | 1997 | 回顧 | Med Clin North Am | 說明 MAC 是 AIDS 最常見的全身性細菌感染，大環內酯類的出現使治療方案大幅進步 |
| [23828580](https://pubmed.ncbi.nlm.nih.gov/23828580/) | 2013 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | 比較 rifamycin 與 isoniazid 預防結核，對象為 HIV 陰性者，與 HIV 患者間接相關 |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | 回顧 | Microbiol Spectr | 說明 HIV 與結核病互相加劇，並探討共治療的挑戰 |
| [30217608](https://pubmed.ncbi.nlm.nih.gov/30217608/) | 2018 | 病例報告 | J Fr Ophtalmol | 一名感染 HIV 的 10 歲兒童出現 rifabutin 相關葡萄膜炎，屬安全性訊號 |

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-38559 | MYCOBUTIN CAP 150MG | PFIZER CORPORATION HONG KONG LIMITED |

## 安全性考量

資料中的警語、禁忌症與藥物交互作用查詢結果皆為空，詳細內容請參考原廠仿單。以下是從臨床證據中看到的重點：

- **嗜中性白血球低下**：兒童研究（PMID 31139825、33294914）曾出現需停藥的嗜中性白血球低下，需定期監測血球。
- **葡萄膜炎**：有 HIV 兒童發生 rifabutin 相關葡萄膜炎的病例報告（PMID 30217608），用藥期間需留意眼部症狀。
- **肝毒性**：需監測肝功能。
- **CYP3A4 交互作用**：多項試驗顯示 rifabutin 與蛋白酶抑制劑（如 lopinavir/ritonavir、nelfinavir）及其他抗病毒藥併用時，需調整劑量並監測藥物濃度。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多個已完成的 Phase 3 隨機試驗（如 NCT00002122、NCT00001030、NCT00001047、NCT00002101），支持 rifabutin 用於 HIV 患者的 MAC 預防與治療，證據等級為 L1。
- 這些證據只涵蓋 HIV 相關分枝桿菌感染，不涵蓋 HIV 本身。香港已有 1 張上市許可證，但資料中沒有其核准適應症文字。

**若要推進需要：**
- 將適應症限定為「HIV 相關分枝桿菌感染（MAC 預防/治療、HIV/結核共感染）」，不宣稱可治療 HIV 本身。
- 取得香港衛生署許可證的核准適應症與仿單，確認警語與禁忌症。
- 補充 DrugBank 的作用機轉與交互作用資料，並建立與抗病毒藥併用的劑量調整指引。
- 建立嗜中性白血球低下、葡萄膜炎與肝毒性的監測計畫，兒童族群尤其需要。

**其他預測適應症：** TxGNN 另預測了多發性內分泌腫瘤、硬化性膽管炎、一種罕見神經發育疾患與結膜炎，目前皆為 **Hold**。這些預測沒有臨床試驗支持，也找不到合理的機轉關聯。結膜炎唯一的文獻是藥物引起眼部發炎的回顧，應視為安全性警訊，不是療效證據。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選須經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

